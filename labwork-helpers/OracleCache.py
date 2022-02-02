# License: CC-0

import hashlib
import json
import contextlib
import requests

class OracleCache():
	def __init__(self, oracle_uri):
		self._uri = oracle_uri
		self._sess = requests.Session()
		self._ora_cachefile = "ora_cache_" + hashlib.md5(oracle_uri.encode()).hexdigest() + ".json"
		try:
			with open(self._ora_cachefile) as f:
				self._cache = json.load(f)
		except (FileNotFoundError, json.decoder.JSONDecodeError):
			self._cache = { }
			self.write_cache()
		self._query_count = 0

	@property
	def query_count(self):
		return self._query_count

	def write_cache(self):
		with open(self._ora_cachefile, "w") as f:
			json.dump(self._cache, f, separators = (",", ":"))

	def _execute(self, query):
		self._query_count += 1
		response = self._sess.post(self._uri, headers = {
			"Content-Type": "application/json",
		}, data = json.dumps(query))

		if response.status_code == 200:
			response_data = response.json()
			return response_data
		else:
			raise Exception("Oracle responded with Turbogrütze: %s / %s" % (response, response.content))

	def execute(self, query):
		key = json.dumps(query, sort_keys = True, separators = (",", ":"))
		if key in self._cache:
			return self._cache[key]
		response = self._execute(query)
		self._cache[key] = response
		return response

	def __enter__(self):
		return self

	def __exit__(self, *args):
		self.write_cache()

if __name__ == "__main__":
	# This is how you use this. Be careful that you DO NOT hardcode the URI
	# (like shown below), but use the command line argument instead.
	with OracleCache("https://127.0.0.1:5000/oracle/pkcs7_padding") as oc:
		print(oc.execute({ "keyname": "bar", "ciphertext": "mEQRQd7KTbo7mRQZ4dTKzg==", "iv": "mEQRQd7KTbo7mRQZ4dTKzg==" }))
