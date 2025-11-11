import os
import subprocess
import json
import wave
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
import tempfile

def download_audio_with_ytdlp(url, output_path="audio"):
    """Скачивает аудио с YouTube используя youtube-dlp"""
    try:
        # Команда для скачивания аудио в лучшем качестве и конвертации в mp3
        command = [
            "youtube-dlp",
            "-x",  # извлечь аудио
            "--audio-format", "mp3",  # формат аудио
            "--audio-quality", "0",  # лучшее качество
            "-o", f"{output_path}.%(ext)s",  # выходной файл
            url
        ]
        
        print("Скачивание аудио с YouTube...")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Аудио успешно скачано!")
        
        return f"{output_path}.mp3"
    
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при скачивании: {e}")
        print(f"Stderr: {e.stderr}")
        return None

def convert_audio_for_vosk(audio_path):
    """Конвертирует аудио в формат, подходящий для Vosk"""
    try:
        print("Конвертация аудио для распознавания...")
        
        # Загружаем аудио
        audio = AudioSegment.from_file(audio_path)
        
        # Конвертируем в формат для Vosk: 16000 Hz, моно, 16-bit
        audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
        
        # Создаем временный файл
        temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        temp_wav_path = temp_wav.name
        temp_wav.close()
        
        # Экспортируем в WAV
        audio.export(temp_wav_path, format="wav")
        
        return temp_wav_path
    
    except Exception as e:
        print(f"Ошибка при конвертации аудио: {e}")
        return None

def transcribe_audio_vosk(wav_path, model_path="model"):
    """Транскрибирует аудио используя Vosk"""
    try:
        # Проверяем наличие модели
        if not os.path.exists(model_path):
            print(f"Модель Vosk не найдена в папке: {model_path}")
            print("Скачайте модель с https://alphacephei.com/vosk/models")
            print("Например: vosk-model-en-us-0.22 (английская) или vosk-model-ru-0.42 (русская)")
            return None
        
        print("Загрузка модели Vosk...")
        model = Model(model_path)
        
        print("Начало распознавания...")
        wf = wave.open(wav_path, "rb")
        
        # Проверяем формат аудио
        if (wf.getnchannels() != 1 or 
            wf.getsampwidth() != 2 or 
            wf.getframerate() not in [8000, 16000, 32000, 48000]):
            print("Неверный формат аудио. Требуется: WAV, моно, 16-bit, 16kHz")
            return None
        
        # Создаем распознаватель
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)  # Включаем распознавание слов с временными метками
        
        results = []
        print("Обработка аудио...")
        
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if 'text' in result and result['text']:
                    results.append(result['text'])
                    print(f"Распознано: {result['text']}")
        
        # Получаем финальный результат
        final_result = json.loads(rec.FinalResult())
        if 'text' in final_result and final_result['text']:
            results.append(final_result['text'])
        
        full_text = ' '.join(results)
        return full_text
    
    except Exception as e:
        print(f"Ошибка при распознавании: {e}")
        return None

def main():
    """Основная функция"""
    print("=== YouTube Video to Text Converter ===")
    print("Используется youtube-dlp и Vosk для распознавания речи")
    
    # Получаем URL от пользователя
    youtube_url = input("Введите URL YouTube видео: ").strip()
    
    if not youtube_url:
        print("URL не может быть пустым!")
        return
    
    # Создаем временную директорию для файлов
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # Шаг 1: Скачиваем аудио
            audio_path = os.path.join(temp_dir, "audio")
            downloaded_audio = download_audio_with_ytdlp(youtube_url, audio_path)
            
            if not downloaded_audio or not os.path.exists(downloaded_audio):
                print("Не удалось скачать аудио!")
                return
            
            # Шаг 2: Конвертируем аудио
            wav_path = convert_audio_for_vosk(downloaded_audio)
            if not wav_path:
                print("Не удалось конвертировать аудио!")
                return
            
            # Шаг 3: Распознаем речь
            # Укажите путь к вашей модели Vosk
            model_path = "model"  # Измените на ваш путь если нужно
            
            text = transcribe_audio_vosk(wav_path, model_path)
            
            # Выводим результат
            if text:
                print("\n" + "="*50)
                print("РАСПОЗНАННЫЙ ТЕКСТ:")
                print("="*50)
                print(text)
                
                # Сохраняем в файл
                output_file = "transcribed_text.txt"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"\nТекст также сохранен в файл: {output_file}")
            else:
                print("Не удалось распознать текст!")
        
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()