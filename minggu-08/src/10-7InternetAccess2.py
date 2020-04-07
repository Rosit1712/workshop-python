import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('goblinslayes@contoh.org', 'jcaesar@contoh.org',
"""To: jcaesar@contoh.org
From: goblinslayes@contoh.org

Beware the Ides of March.
""")
server.quit()