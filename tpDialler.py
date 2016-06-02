import telnetlib
import os
import click


@click.command()
@click.argument("ip")
@click.argument("number")
@click.option("--username", help="Endpoint's Telnet User")
@click.option("--password", help="Endpoint's Telnet Password")
def make_call(number, ip, username=os.environ["USER"], password=""):
    username = username.encode()
    password = password.encode()
    number = number.encode()
    tn = telnetlib.Telnet(ip)
    tn.read_until("login: ")
    tn.write(username + "\n")
    tn.read_until("Password: ")
    tn.write(password + "\n")
    tn.read_until("OK")
    tn.write("xCommand Dial Number:\"" + number + "\" Protocol:sip\n")
    tn.read_until("OK")
    tn.close()

