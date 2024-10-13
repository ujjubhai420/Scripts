
#Just paste the file in the parent folder that contain the folder you want to organise

from pathlib import Path

def traverse_dir(dir_name):
    dir_path=Path(dir_name)        
    for x in dir_path.glob('*'):
        if(x.is_dir()):
            traverse_dir(x)
        else:
            if x.suffix in photos:
                move_files(x,photos_dir)
            elif x.suffix in videos:
                move_files(x,video_dir)

def create_directory(dir_name):
    dir_path=Path(dir_name)
    dir_path.mkdir(exist_ok=True)
    return dir_path

def move_files(file_path,dest_dir):
    try:
     file=Path(file_path)
     dest_path=Path(dest_dir) 
     new_dest=dest_path /file.name  
     if new_dest.exists():
         print(f"File '{file.name}'already exists in '{dest_path}'.Deleting the duplicate")
         file.unlink()
     else:    
         file.rename(new_dest)
         print(f"Moved '{file.name}'to '{dest_path}'")
    except Exception as e:
     
        print(f"Error occured '{file_path}':{e} ")           

photos=['.jpg','.png']
videos=['.mp4']

photos_dir=create_directory("Photos")
video_dir=create_directory("Videos")
wd=Path('./')#Insert the path for the folder you want to organise
traverse_dir(wd)

