import os
import pathlib
from pydub import AudioSegment

file_path = os.path.dirname(__file__)
input_path = os.path.join(file_path,"input")
output_path = os.path.join(file_path,"output")
pathlib.Path(input_path).mkdir(parents=True, exist_ok=True) 
bank_template_path = os.path.join(input_path,"Bank Template")
pathlib.Path(bank_template_path).mkdir(parents=True, exist_ok=True) 
pathlib.Path(os.path.join(bank_template_path,"01. Bass Drum")).mkdir(parents=True, exist_ok=True) 
pathlib.Path(os.path.join(bank_template_path,"02. Bass Drum")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"03. Bass Drum")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"04. Bass Drum")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"05. Snare Drum")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"06. Snare Drum")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"07. Snare Drum - Rim Shot")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"08. Snare Drum - Clap")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"09. CH")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"10. OH")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"11. Crash")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"12. Other")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"13. Tom Hi")).mkdir(parents=True, exist_ok=True)
pathlib.Path(os.path.join(bank_template_path,"14. Tom Low")).mkdir(parents=True, exist_ok=True)

pathlib.Path(output_path).mkdir(parents=True, exist_ok=True) 

bank_list = os.scandir(input_path)

file_enum = 1
dummy_loop = 1

for entry_bank in bank_list:
	if entry_bank.is_dir:
		for entry_category in os.scandir(entry_bank):
			file_list = os.scandir(entry_category)
			for entry_file in file_list:
				# If the trigger would be 15 or 16, create a new dummy wav with silence
				# for the two triggers that are used for bank up/down

				if dummy_loop == 15:
					sound = AudioSegment.silent(duration=1000)
					output_file_path = os.path.join(output_path,str(file_enum).zfill(3) + " " + "dummy.wav")
					file_handle = sound.export(output_file_path, format="wav")
					file_enum += 1
					dummy_loop += 1
				if dummy_loop == 16:
					sound = AudioSegment.silent(duration=1000)
					output_file_path = os.path.join(output_path,str(file_enum).zfill(3) + " " + "dummy.wav")
					file_handle = sound.export(output_file_path, format="wav")
					file_enum += 1
					dummy_loop = 1


				# Stereoizes files if they were mono
				sound = AudioSegment.from_file(entry_file.path, format="wav")
				# Changes the sample rate
				sound = sound.set_frame_rate(44100)
				# Creates duplicate stereo channel if does not exist
				sound = sound.set_channels(2)
				# Sets it to be 16-bit
				sound = sound.set_sample_width(2)

				# Copies to output, and renames the copy.
				output_file_path = os.path.join(output_path,str(file_enum).zfill(3) + " " + entry_file.name)
				file_handle = sound.export(output_file_path, format="wav")

				print(output_file_path)
				file_enum += 1
				dummy_loop += 1

if file_enum > 1:
	# Creates Dummy WAVs for the final two triggers
	sound = AudioSegment.silent(duration=1000)
	output_file_path = os.path.join(output_path,str(file_enum).zfill(3) + " " + "dummy.wav")
	file_handle = sound.export(output_file_path, format="wav")
	file_enum += 1
	output_file_path = os.path.join(output_path,str(file_enum).zfill(3) + " " + "dummy.wav")
	file_handle = sound.export(output_file_path, format="wav")






