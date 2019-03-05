import os
import requests

def download_file(url, local_filename=None):
	if local_filename is None:
		local_filename = url.split('/')[-1]

	if os.path.exists(local_filename):
		return	local_filename

	if not url.startswith('http'):
		url = 'http:'+url

	r = requests.get(url,stream=True)
	with open(local_filename,'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
	return local_filename