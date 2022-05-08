import logging

# Par défaut, seul les messages de niveau WARNING et plus élevés sont affichés
# Pour afficher tous les messages, on change le niveau de logging
# logging.basicConfig(level=logging.DEBUG)

# On rajoute un format d'affichage avec l'heure, le niveau de log et le message
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# On va écrire les logs dans un fichier
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='log_file.log', filemode='a')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')