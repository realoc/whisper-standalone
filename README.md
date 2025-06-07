# Whisper Standalone
Whisper Standalone is a wrapper for [openai whisper](https://github.com/openai/whisper) to provide a more accessible version for non-developers.
This is a command line tool that includes all dependencies including python.

## Installation
Download the appropriate standalone for your OS from the latest [release](https://github.com/realoc/whisper-standalone/releases).
Simply extract the archive and you are good to go.

## Usage
Open a Terminal and navigate the folder that contains the extracted whisper standalone.
Run the tool similar to the full example for your OS.
The tool expects two arguments: language to transcribe to and path to the audio file.
As it is a wrapper of openai whisper it supports the same audio file formats: flac, mp3 and wav.
### language
Can be [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) or English name of the language e.g. `es` or `Spanish`.
### path
Either absolute or relative e.g. for MacOS `~/Downloads/file-to-transcribe.mp3` or for Windows based `C:\Users\yourUserName\Downloads\file-to-transcribe.mp3`
### Full example
#### Windows
``.\whisper_standalone.exe es C:\Users\YourUserName\Downloads\audio-file-to-transcribe.mp3``
#### MacOS
``
whisper_standaline-macos es ~/Downloads/audio-file-to-transcribe.mp3
``