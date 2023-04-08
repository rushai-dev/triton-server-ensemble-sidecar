from fastapi import HTTPException

class json_request():

    def __init__(self, _json):
        if not _json.get("inputs"):
            raise HTTPException(status_code=404, detail="inputs not found")
        self._json = _json

    async def get(self):

        return self._json.get("inputs")


class multi_form_data_request():
    
    def __init__(self, form):
        if not form.getlist("inputs"):
            raise HTTPException(status_code=404, detail="inputs not found")
        self.form = form

    async def get(self):
        payloads = []
        for _file in self.form.getlist("inputs"):
            
            file = await _file.read()
  
            _dict = {
                "filename": _file.filename,
                "content-type": _file.content_type,
                "content-bytes": file
            }
            payloads.append(_dict)

        _json = {
          "inputs": payloads
        }
                
        return _json
