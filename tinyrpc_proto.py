
class ProtoSuccessResponse(RPCResponse):
    def _to_dict(self):
        return {
            #'jsonrpc': JSONRPCProtocol.JSON_RPC_VERSION,
            'id': self.unique_id,
            'result': self.result,
        }

    def serialize(self):
    	# TODO
        return json.dumps(self._to_dict())

class ProtoErrorResponse(RPCErrorResponse):
    def _to_dict(self):
        return {
            #'jsonrpc': JSONRPCProtocol.JSON_RPC_VERSION,
            'id': self.unique_id,
            'error': {
                'message': str(self.error),
                #'code': self._jsonrpc_error_code,
            }
        }

    def serialize(self):
        # TODO
        return json.dumps(self._to_dict())

class ProtoRequest(tinyrpc.RPCRequest):
    def error_respond(self, error):
        if not self.unique_id:
            return None

        response = ProtoErrorResponse()

        #code, msg = _get_code_and_message(error)
        code , msg = 10, "error"

        response.error = msg
        response.unique_id = self.unique_id
        response._jsonrpc_error_code = code
        return response

    def respond(self, result):
        response = ProtoSuccessResponse()

        if not self.unique_id:
            return None

        response.result = result
        response.unique_id = self.unique_id

        return response

    def _to_dict(self):
        jdata = {
            #'jsonrpc': JSONRPCProtocol.JSON_RPC_VERSION,
            'method': self.method,
        }
        if self.args:
            jdata['params'] = self.args
        if self.kwargs:
            jdata['params'] = self.kwargs
        if self.unique_id != None:
            jdata['id'] = self.unique_id
        return jdata

    def serialize(self):
        return json.dumps(self._to_dict())

class ProtoProtocol(tinyrpc.RPCProtocol):
    def _get_unique_id(self):
        self._id_counter += 1
        return self._id_counter
    def create_request(method,args=None,kwargs=None,one_way=False):
    	if args and kwargs:
            raise InvalidRequestError('Does not support args and kwargs at '\
                                      'the same time')
		# -> RPCRequest
		request = ProtoRequest()
        if not one_way:
            request.unique_id = self._get_unique_id()
        request.method = method
        request.args = args
        request.kwargs = kwargs
        return request
	def parse_reply(data):
		#string -> ProtoErrorResponse ProtoSuccessResponse
		pass
	def parse_request(data):
		# batch requests are LIST
		# ...InvalidRequestError
		# ...InvalidParamsError
		#string -> JSONRPCSuccessResponse
		#_ALLOWED_REQUEST_KEYS
		pass

