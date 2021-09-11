## Getting SSH Log

Data collected from machine running Ubuntu Linux 18.04.

```
$ cat /var/log/auth.log > auth.log
```

Since `auth.log` contains more than just SSH service logs, and the SSH service logs contain redundant data for the purposes of this project, the logs were further parsed into a CSV containing just the username and ip address of the attempted log in

## Parsing SSH Log into CSV File

The following commands were used to go from the `auth.log` file to a CSV file to be used for this project.  
Problem faced included handling attempts that did not include usernames (just connected attempting an IP)

1. Avoiding duplicate data records by getting only 'Invalid user' reports
```
$ cat auth.log | grep "Invalid user" > auth-invalidusers.log
```
2. Avoiding blank ('') usernames as auth attempts
```
$ cat auth-invalidusers.log | egrep "user \w+" > auth-invalidusers-unames.log
```
3. Parsing out just the ip addresses
```
$ cat auth-invalidusers-unames.log | egrep -o " [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ " | egrep "[0-9]" > auth-ips
```
4. Parsing out just the usernames
```
$ cat auth-invalidusers-unames.log | egrep -o "user .+ from [0-9]" | awk '{print $2}' > auth-usernames
```
5. Merging usernames and IPs into a csv file
```
$ paste auth-usernames auth-ips | awk -F ",||\t" '{print $1","$2}' > auth.logs.csv
```

## Getting JSON data for IP addresses

For each IP, I wanted to map the lat lon coordinates to a map.

Using API `ipinfo.io` to perform lat/lon lookup of given IP address.

Sample usage on command line:
```
curl ipinfo.io/115.56.115.248
```

Using the `python` `response` module, the following will get the json data returned by the API

```
response = requests.get("https://ipinfo.io/"+ip_variable)
print(response.json())
```

API does have a response time limit that - needed to add a wait time delay to query API