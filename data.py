
from __future__ import print_function
import sys, codecs
from hazm import Normalizer, Stemmer


def create_words_file(dic_file='resources/persian.dic', output='hazm/data/words.dat'):
	""" prepares list of persian word words from [Virastyar dic](https://sourceforge.net/projects/virastyar/files/Data/1.3.1/persian.dic/download) file.
	"""

	dic_words = [line.split('\t')[0] for line in codecs.open(dic_file, encoding='utf8')]
	print(*dic_words, sep='\n', file=codecs.open(output, 'w', 'utf8'))
	print(output, 'created')


def create_verbs_file(valency_file='resources/valency.txt', output='hazm/data/verbs.dat'):
	""" prepares list of persian verbs from [Verb Valency](http://dadegan.ir/pervallex) corpus.
	"""

	verbs = []
	for l, line in enumerate(codecs.open(valency_file, encoding='utf8')):
		parts = line.split('\t')
		if l > 1 and len(parts) == 6:
			past, present = parts[0], parts[1]

			if past != '-':
				verb = past+'#'+present
				if verb not in verbs:
					verbs.append(verb)

	print(*verbs, sep='\n', file=codecs.open(output, 'w', 'utf8'))
	print(output, 'created')


if __name__ == '__main__':
	if len(sys.argv) == 2:
		if sys.argv[1] == 'create_words_file':
			create_words_file()
		elif sys.argv[1] == 'create_verbs_file':
			create_verbs_file()