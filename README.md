# Fuzzing_with_Boo
<b>Boofuzz</b> scripts used to fuzz some well know vulnerable applications<br>
To use these scripts you must install boofuzz from source: https://boofuzz.readthedocs.io/en/stable/user/install.html#from-source
1. <i>bFuzzPCManFTP.py</i> get the vulnerable app from<br>https://www.exploit-db.com/apps/9fceb6fefd0f3ca1a8c36e97b6cc925d-PCMan.7z
2. <i>bFuzzVulnserver.py</i> get the server from<br>https://github.com/stephenbradshaw/vulnserver
3. <i>bFuzzWarFTPD.py</i> get the app from<br>https://www.exploit-db.com/apps/5132d652476f071874e42023e66dc1c1-WarFTP165_vulnerable_USER_BufferOverflow.exe

# Analyze results
The results are saved in <b>boofuzz-results</b> folder from where the script has been executed, as <b>sqlite database file</b>. We can use SQLite data browser to inspect the test results, <b>steps</b> are saved into the same name table.
![Sqlite Browser](/images/boofuzz-result.png)
The previous example assumes that the vulnerable application crashed during the test case number <b>157</b> injecting  <b>100002</b> bytes as shown in the image above

# Documentation
https://boofuzz.readthedocs.io/en/stable/index.html
