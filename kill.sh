ps aux | grep python | grep fetch | awk '{print $2}' | xargs kill -9
