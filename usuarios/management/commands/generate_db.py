from django.core.management import BaseCommand
import os

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--full', '-f', action= "store_true")
        parser.add_argument('--make', '-m', action= "store_true")
    
    def handle(self, *args, **options):
        score = int(0)
        if not options.get('full'):
            try:
                os.system('python manage.py sqlflush')
            except:
                self.stdout.write(self.style.ERROR('Erro ao recaregar o banco de dados'))
                self.stdout.write(self.style.WARNING('Tente:'))
                self.stdout.write(self.style.WARNING('    -> Parar a aplicação;'))
                self.stdout.write(self.style.WARNING('    -> Desconetar o banco de dados.'))
            print('')
            self.stdout.write(self.style.SUCCESS('Banco de dados recarregado com sucesso'))
        else:
            if os.path.exists('db.sqlite3'):
                try:
                    os.remove('db.sqlite3')
                except:
                    self.stdout.write(self.style.ERROR('Bando de dados está em execução'))
                    self.stdout.write(self.style.WARNING('Tente:'))
                    self.stdout.write(self.style.WARNING('    -> Parar a aplicação;'))
                    self.stdout.write(self.style.WARNING('    -> Desconetar o banco de dados.'))
                    score = 1
                if score == 0:
                    self.stdout.write(self.style.SUCCESS('Banco de dados excluido'))
                    print('')
            if score == 0:
                if not options.get('make'):
                    os.system('python manage.py migrate')
                    print('')
                    self.stdout.write(self.style.SUCCESS('Banco de dados gerado com sucesso'))
                else:
                    os.system('python manage.py makemigrations')
                    self.stdout.write(self.style.SUCCESS('Gerando as migrações'))
                    os.system('python manage.py migrate')
                    print('')
                    self.stdout.write(self.style.SUCCESS('Banco de dados gerado com sucesso'))