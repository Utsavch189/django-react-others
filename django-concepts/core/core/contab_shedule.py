from django.core.management import call_command

def db_backUp():
  try:
    call_command('dbbackup')
  except:
    pass