import os, time
from scrapli.driver.core import JunosDriver
from scrapli.exceptions import ScrapliException
import ntc_templates

# tell TextFSM where templates live
#os.environ["NET_TEXTFSM"] = os.path.join(    os.path.dirname(ntc_templates.__file__), "templates")

start = time.perf_counter()

device = {
    "host": "10.5.5.8",
    "auth_username": "sntuser",
    "auth_password": "Ilovenetworks99",
    "auth_strict_key": False,
    "transport": "ssh2",   # or "paramiko"
    "timeout_ops": 30,
}
try:
    with JunosDriver(**device) as conn:
        resp = conn.send_command("show version")  # keep it plain (no pipes) for TextFSM
        parsed = resp.textfsm_parse_output()
       
        print("\n===== parsed (TextFSM) =====")
        if parsed:
            # list of dicts; print first row nicely
            for k, v in parsed[0].items():
                print(f"{k}: {v}")
        else:
            print("(no TextFSM match)")

        print("\n===== raw =====\n")
        print(resp.result)

        print(f"\nTook {time.perf_counter() - start:.4f} s")
except ScrapliException as e:
    print(f"Error: {e}")
    