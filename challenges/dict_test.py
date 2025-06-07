
config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : "12345"
}
print(f'Number of elements in config is {len(config)}')
print(f'Value for fbType is {config["dbType"]}')

for key, value in config.items():
    print(f'Key in config: {key} with vaule {value}')