# spotify_metadata
Get basic metadata of songs by their Sptify-Track-ID. **If you are looking for a real solution check out spotipy (https://github.com/plamere/spotipy)!**


## needed dependencies

* re (comes with python)
* requests
  * can be installed using ```pip install requests```
* lxml
  * can be installed using ```pip isntall lxml```


## how to use

### from the commandline
On Linux and MacOS: 
```python3 metadata_by_track_id.py <TRACK_ID>```<br>
On Windows: 
```python metadata_by_track_id.py <TRACK_ID>```

### from within python
```python3
from metadata_by_track_id import metadata
response=metadata(TRACK_ID)
```
