from pydub import AudioSegment
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

AUDIO_PATH = 'audio/'
M4A_PATH = AUDIO_PATH + 'm4a/'
WAV_PATH = AUDIO_PATH + 'wav/'

files_in_m4a_path = next((filename for filename in os.walk(M4A_PATH)),
                         (None, None, []))
m4a_filenames = [filename for filename in files_in_m4a_path[2] if '.m4a' in filename]

if m4a_filenames:
    logger.info(f'Found [{len(m4a_filenames)}] .m4a files at [{M4A_PATH}] to transform to wav. '
                f'Starting transforming m4a files to wav to [{WAV_PATH}]...')

    wav_files_saved = 0
    for m4a_filename in m4a_filenames:
        wav_filename = WAV_PATH + m4a_filename.replace('m4a', 'wav')

        if os.path.isfile(wav_filename):
            logging.warning(f'Skipped [{wav_filename}] as it already exists')
        else:
            m4a_file = AudioSegment.from_file(M4A_PATH + m4a_filename, format='m4a')
            logging.info(f'Transforming to [{wav_filename}]...')
            m4a_file.export(wav_filename, format='wav')
            wav_files_saved += 1

    if wav_files_saved:
        logging.info(f'[{wav_files_saved}] file saved')
    else:
        logging.warning('No new wav files saved')
else:
    logger.warning(f'No files found at m4a path [{M4A_PATH}]')
