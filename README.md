# darwin.py
Quick and dirty subscription to darwin push port. 

Usage:

1. Install pip
2. Install stomp
```bash
pip install stomp.py
```
3. Run script
```bash
python darwin.py stomp_username stomp_password queue_name
```
You can grab stomp_username, stomp_password and queue_name by signing up to https://datafeeds.nationalrail.co.uk. 

Default timeout set to 1s. Fork/copy it all you need to.

More details on Darwin push port at http://nrodwiki.rockshore.net/index.php/Darwin:Push_Port