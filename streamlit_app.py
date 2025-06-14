[     UTC     ] Logs for token30listener-7vtsmxcgqzmcyzaatzcrbz.streamlit.app/

────────────────────────────────────────────────────────────────────────────────────────

[12:14:33] 🚀 Starting up repository: 'token30_listener', branch: 'main', main module: 'streamlit_app.py'

[12:14:33] 🐙 Cloning repository...

[12:14:34] 🐙 Cloning into '/mount/src/token30_listener'...

[12:14:34] 🐙 Cloned repository!

[12:14:34] 🐙 Pulling code changes from Github...

[12:14:34] 📦 Processing dependencies...


──────────────────────────────────────── uv ───────────────────────────────────────────


Using uv pip install.

Using Python 3.13.5 environment at /home/adminuser/venv

Resolved 57 packages in 688ms

Prepared 57 packages in 2.21s

Installed 57 packages in 72ms

 + aiodns==3.5.0

 + aiohappyeyeballs==2.6.1

 + aiohttp==3.12.12

 + aiosignal==1.3.2

 + altair==5.5.0

 + attrs==25.3.0

 + blinker==1.9.0

 + cachetools==5.5.2

 + ccxt==4.4.89

 +[2025-06-14 12:14:38.046521]  certifi==2025.4.26

 + cffi==1.17.1

 + charset-normalizer==3.4.2

 + click==8.2.1

 + cryptography==45.0.4

 + dateparser==1.2.1

 + [2025-06-14 12:14:38.046784] frozenlist==1.7.0

 + gitdb==4.0.12

 + gitpython==3.1.44

 + idna==3.10

 + jinja2==3.1.6

 + jsonschema==4.24.0

 + [2025-06-14 12:14:38.046956] jsonschema-specifications==2025.4.1

 + markupsafe==3.0.2

 + multidict==6.4.4

 + narwhals==1.42.1

 + numpy==2.3.0

 + packaging==24.2

 + [2025-06-14 12:14:38.047151] pandas==2.3.0

 + pillow==11.2.1

 + propcache==0.3.2

 + protobuf==6.31.1[2025-06-14 12:14:38.047376] 

 + pyarrow==20.0.0

 + pycares==4.9.0

 + pycparser==2.22

 + pycryptodome==3.23.0

 + pydeck[2025-06-14 12:14:38.047528] ==0.9.1

 + python-binance==1.0.29

 + python-dateutil==2.9.0.post0

 + pytz==2025.2

 + referencing[2025-06-14 12:14:38.047645] ==0.36.2

 + regex==2024.11.6

 + requests==2.32.4

 + rpds-py==0.25.1

 + setuptools==80.9.0

 + six[2025-06-14 12:14:38.047748] ==1.17.0

 + smmap==5.0.2

 + streamlit==1.45.1

 + tenacity==9.1.2

 + toml[2025-06-14 12:14:38.047849] ==0.10.2

 + tornado==6.5.1

 + typing-extensions==4.14.0

 + tzdata==2025.2

 [2025-06-14 12:14:38.047945] + tzlocal==5.3.1

 + urllib3==2.4.0

 + watchdog==6.0.0

 + websockets==15.0.1

 + yarl==1.20.1

Checking if Streamlit is installed

Found Streamlit version 1.45.1 in the environment

Installing rich for an improved exception logging

Using uv pip install.

Using Python 3.13.5 environment at /home/adminuser/venv

Resolved 4 packages in 116ms

Prepared 4 packages in 101ms

Installed 4 packages in 11ms

 + markdown-it-py==3.0.0

 + mdurl==0.1.2

 + pygments==2.19.1

 + rich==14.0.0


────────────────────────────────────────────────────────────────────────────────────────


[12:14:40] 🐍 Python dependencies were installed from /mount/src/token30_listener/requirements.txt using uv.

Check if streamlit is installed

Streamlit is already installed

[12:14:41] 📦 Processed dependencies!




────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

[12:19:41] ❗️ 

2025-06-14 12:19:41.663 503 GET /script-health-check (127.0.0.1) 6811.69ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:19:44.540 503 GET /script-health-check (127.0.0.1) 2625.20ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:19:47.499 503 GET /script-health-check (127.0.0.1) 2644.95ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:19:52.537 503 GET /script-health-check (127.0.0.1) 2676.04ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:19:57.504 503 GET /script-health-check (127.0.0.1) 2657.00ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:02.520 503 GET /script-health-check (127.0.0.1) 2674.05ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:07.526 503 GET /script-health-check (127.0.0.1) 2671.87ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:12.534 503 GET /script-health-check (127.0.0.1) 2679.16ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:17.456 503 GET /script-health-check (127.0.0.1) 2607.19ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:22.528 503 GET /script-health-check (127.0.0.1) 2678.05ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:27.515 503 GET /script-health-check (127.0.0.1) 2669.62ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:32.538 503 GET /script-health-check (127.0.0.1) 2670.93ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:37.527 503 GET /script-health-check (127.0.0.1) 2670.62ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:42.564 503 GET /script-health-check (127.0.0.1) 2687.18ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:47.518 503 GET /script-health-check (127.0.0.1) 2675.78ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:52.463 503 GET /script-health-check (127.0.0.1) 2622.25ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:20:57.466 503 GET /script-health-check (127.0.0.1) 2621.52ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:02.517 503 GET /script-health-check (127.0.0.1) 2671.31ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:07.530 503 GET /script-health-check (127.0.0.1) 2679.09ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:12.466 503 GET /script-health-check (127.0.0.1) 2612.86ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:17.493 503 GET /script-health-check (127.0.0.1) 2647.53ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:22.544 503 GET /script-health-check (127.0.0.1) 2691.36ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:27.453 503 GET /script-health-check (127.0.0.1) 2612.26ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:32.534 503 GET /script-health-check (127.0.0.1) 2672.24ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:37.469 503 GET /script-health-check (127.0.0.1) 2615.06ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:42.603 503 GET /script-health-check (127.0.0.1) 2737.40ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:47.477 503 GET /script-health-check (127.0.0.1) 2637.25ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:52.570 503 GET /script-health-check (127.0.0.1) 2712.15ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:21:57.472 503 GET /script-health-check (127.0.0.1) 2624.31ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:02.565 503 GET /script-health-check (127.0.0.1) 2716.68ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:10.408 503 GET /script-health-check (127.0.0.1) 5559.96ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:13.515 503 GET /script-health-check (127.0.0.1) 2853.01ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:17.702 503 GET /script-health-check (127.0.0.1) 2855.53ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:22.792 503 GET /script-health-check (127.0.0.1) 2953.09ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:27.721 503 GET /script-health-check (127.0.0.1) 2884.34ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:32.719 503 GET /script-health-check (127.0.0.1) 2856.81ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:37.791 503 GET /script-health-check (127.0.0.1) 2943.58ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:45.276 503 GET /script-health-check (127.0.0.1) 5432.10ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:48.105 503 GET /script-health-check (127.0.0.1) 2569.80ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:54.139 503 GET /script-health-check (127.0.0.1) 4263.24ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:22:57.736 503 GET /script-health-check (127.0.0.1) 2892.14ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:02.802 503 GET /script-health-check (127.0.0.1) 2932.14ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:07.744 503 GET /script-health-check (127.0.0.1) 2901.97ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:12.715 503 GET /script-health-check (127.0.0.1) 2875.08ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:17.687 503 GET /script-health-check (127.0.0.1) 2846.72ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:22.814 503 GET /script-health-check (127.0.0.1) 2968.10ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:27.727 503 GET /script-health-check (127.0.0.1) 2878.84ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:32.702 503 GET /script-health-check (127.0.0.1) 2857.98ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:37.715 503 GET /script-health-check (127.0.0.1) 2861.91ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:42.776 503 GET /script-health-check (127.0.0.1) 2930.70ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:47.725 503 GET /script-health-check (127.0.0.1) 2881.84ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:52.834 503 GET /script-health-check (127.0.0.1) 2979.87ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:23:57.722 503 GET /script-health-check (127.0.0.1) 2874.22ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:24:02.769 503 GET /script-health-check (127.0.0.1) 2928.51ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:24:07.771 503 GET /script-health-check (127.0.0.1) 2925.95ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:24:12.729 503 GET /script-health-check (127.0.0.1) 2874.70ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:24:17.753 503 GET /script-health-check (127.0.0.1) 2904.53ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:24:22.733 503 GET /script-health-check (127.0.0.1) 2880.72ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:24:27.729 503 GET /script-health-check (127.0.0.1) 2885.90ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:24:32.739 503 GET /script-health-check (127.0.0.1) 2896.79ms

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:582   

  in fetch                                                                      

                                                                                

     579 │   │   │   if self.verbose:                                           

     580 │   │   │   │   self.log("\nfetch Response:", self.id, method, url, h  

     581 │   │   │   self.logger.debug("%s %s, Response: %s %s %s", method, ur  

  ❱  582 │   │   │   response.raise_for_status()                                

     583 │   │                                                                  

     584 │   │   except Timeout as e:                                           

     585 │   │   │   details = ' '.join([self.id, method, url])                 

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/requests/models.py:1026 in  

  raise_for_status                                                              

                                                                                

    1023 │   │   │   )                                                          

    1024 │   │                                                                  

    1025 │   │   if http_error_msg:                                             

  ❱ 1026 │   │   │   raise HTTPError(http_error_msg, response=self)             

    1027 │                                                                      

    1028 │   def close(self):                                                   

    1029 │   │   """Releases the connection back to the pool. Once this method  

────────────────────────────────────────────────────────────────────────────────

HTTPError: 451 Client Error:  for url: 

https://api.binance.com/api/v3/exchangeInfo


During handling of the above exception, another exception occurred:


────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:121 in exec_func_with_error_handling                        

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:645 in code_to_exec                                     

                                                                                

  /mount/src/token30_listener/streamlit_app.py:84 in <module>                   

                                                                                

     81 │   │   │   latest = since                                              

     82 │   │   │   limit = 1000                                                

     83 │   │   │   while latest < now:                                         

  ❱  84 │   │   │   │   ohlcv = ex.fetch_ohlcv('BTC/USDT', interval, since=lat  

     85 │   │   │   │   if not ohlcv:                                           

     86 │   │   │   │   │   break                                               

     87 │   │   │   │   all_ohlcv += ohlcv                                      

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:4446 in     

  fetch_ohlcv                                                                   

                                                                                

     4443 │   │   :param boolean [params.paginate]: default False, when True w  

     4444 │   │   :returns int[][]: A list of candles ordered, open, high, low  

     4445 │   │   """                                                           

  ❱  4446 │   │   self.load_markets()                                           

     4447 │   │   paginate = False                                              

     4448 │   │   paginate, params = self.handle_option_and_params(params, 'fe  

     4449 │   │   if paginate:                                                  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1543  

  in load_markets                                                               

                                                                                

    1540 │   │   if self.has['fetchCurrencies'] is True:                        

    1541 │   │   │   currencies = self.fetch_currencies()                       

    1542 │   │   │   self.options['cachedCurrencies'] = currencies              

  ❱ 1543 │   │   markets = self.fetch_markets(params)                           

    1544 │   │   if 'cachedCurrencies' in self.options:                         

    1545 │   │   │   del self.options['cachedCurrencies']                       

    1546 │   │   return self.set_markets(markets, currencies)                   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:3040 in     

  fetch_markets                                                                 

                                                                                

     3037 │   │   for i in range(0, len(fetchMarkets)):                         

     3038 │   │   │   marketType = fetchMarkets[i]                              

     3039 │   │   │   if marketType == 'spot':                                  

  ❱  3040 │   │   │   │   promisesRaw.append(self.publicGetExchangeInfo(params  

     3041 │   │   │   │   if fetchMargins and self.check_required_credentials(  

     3042 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginAllPairs(pa  

     3043 │   │   │   │   │   promisesRaw.append(self.sapiGetMarginIsolatedAll  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/types.py:35 in    

  unbound_method                                                                

                                                                                

     32 │   │   self.config = config                                            

     33 │   │                                                                   

     34 │   │   def unbound_method(_self, params={}):                           

  ❱  35 │   │   │   return _self.request(self.path, self.api, self.method, par  

     36 │   │                                                                   

     37 │   │   self.unbound_method = unbound_method                            

     38                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/binance.py:11336 in    

  request                                                                       

                                                                                

    11333 │   │   return self.safe_value(config, 'cost', 1)                     

    11334 │                                                                     

    11335 │   def request(self, path, api='public', method='GET', params={}, h  

  ❱ 11336 │   │   response = self.fetch2(path, api, method, params, headers, b  

    11337 │   │   # a workaround for {"code":-2015,"msg":"Invalid API-key, IP,  

    11338 │   │   if api == 'private':                                          

    11339 │   │   │   self.options['hasAlreadyAuthenticatedSuccessfully'] = Tr  

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4490  

  in fetch2                                                                     

                                                                                

    4487 │   │   │   │   │   │   if (retryDelay is not None) and (retryDelay !  

    4488 │   │   │   │   │   │   │   self.sleep(retryDelay)                     

    4489 │   │   │   │   │   else:                                              

  ❱ 4490 │   │   │   │   │   │   raise e                                        

    4491 │   │   │   │   else:                                                  

    4492 │   │   │   │   │   raise e                                            

    4493 │   │   return None  # self line is never reached, but exists for c#   

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:4481  

  in fetch2                                                                     

                                                                                

    4478 │   │   self.last_request_url = request['url']                         

    4479 │   │   for i in range(0, retries + 1):                                

    4480 │   │   │   try:                                                       

  ❱ 4481 │   │   │   │   return self.fetch(request['url'], request['method'],   

    4482 │   │   │   except Exception as e:                                     

    4483 │   │   │   │   if isinstance(e, OperationFailed):                     

    4484 │   │   │   │   │   if i < retries:                                    

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:600   

  in fetch                                                                      

                                                                                

     597 │   │   │   details = ' '.join([self.id, method, url])                 

     598 │   │   │   skip_further_error_handling = self.handle_errors(http_sta  

     599 │   │   │   if not skip_further_error_handling:                        

  ❱  600 │   │   │   │   self.handle_http_status_code(http_status_code, http_s  

     601 │   │   │   raise ExchangeError(details) from e                        

     602 │   │                                                                  

     603 │   │   except requestsConnectionError as e:                           

                                                                                

  /home/adminuser/venv/lib/python3.13/site-packages/ccxt/base/exchange.py:1723  

  in handle_http_status_code                                                    

                                                                                

    1720 │   │   codeAsString = str(code)                                       

    1721 │   │   if codeAsString in self.httpExceptions:                        

    1722 │   │   │   ErrorClass = self.httpExceptions[codeAsString]             

  ❱ 1723 │   │   │   raise ErrorClass(self.id + ' ' + method + ' ' + url + ' '  

    1724 │                                                                      

    1725 │   @staticmethod                                                      

    1726 │   def crc32(string, signed=False):                                   

────────────────────────────────────────────────────────────────────────────────

ExchangeNotAvailable: binance GET https://api.binance.com/api/v3/exchangeInfo 

451  {

  "code": 0,

  "msg": "Service unavailable from a restricted location according to 'b. 

Eligibility' in https://www.binance.com/en/terms. Please contact customer 

service if you believe you received this message in error."

}

2025-06-14 12:24:37.688 503 GET /script-health-check (127.0.0.1) 2839.04ms

[12:24:38] 🐙 Pulling code changes from Github...

[12:24:39] 📦 Processing dependencies...

[12:24:39] 📦 Processed dependencies!

[12:24:40] 🔄 Updated app!
