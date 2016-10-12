import string
from textblob import Blobber
from textblob_aptagger import PerceptronTagger
from textblob.taggers import NLTKTagger,PatternTagger

def accuracy(test_set,tagger):
	n_correct=0
	total=0
	tb=Blobber(pos_tagger=tagger)
	for tagged_sentence in test_set:
		raw_sentence = ' '.join([word for word, tag in tagged_sentence])
		#print raw_sentence
		blob = tb(raw_sentence)
		#print blob
		tags = [tag for word, tag in blob.tags]
		#print "Tags-----"+str(tags)
		target_tags = [tag for word, tag in tagged_sentence
                       if tag not in string.punctuation]
		#print "Target-tags-----"+str(target_tags)
		total += len(tags)
		n_correct += sum(1 for i in range(len(tags)) if tags[i] == target_tags[i])
    	return float(n_correct) / total 

if __name__=='__main__':
	test = [[(u'Pierre', u'NNP'), (u'Vinken', u'NNP'), (u',', u','), (u'61', u'CD'),
                (u'years', u'NNS'), (u'old', u'JJ'), (u',', u','), (u'will', u'MD'),
                (u'join', u'VB'), (u'the', u'DT'), (u'board', u'NN'), (u'as', u'IN'),
                (u'a', u'DT'), (u'nonexecutive', u'JJ'), (u'director', u'NN'),
                (u'Nov.', u'NNP'), (u'29', u'CD'), (u'.', u'.')],
            [(u'Mr.', u'NNP'), (u'Vinken', u'NNP'), (u'is', u'VBZ'), (u'chairman', u'NN'),
                (u'of', u'IN'), (u'Elsevier', u'NNP'), (u'N.V.', u'NNP'), (u',', u','),
                (u'the', u'DT'), (u'Dutch', u'NNP'), (u'publishing', u'VBG'),
                (u'group', u'NN'), (u'.', u'.'), (u'Rudolph', u'NNP'), (u'Agnew', u'NNP'),
                (u',', u','), (u'55', u'CD'), (u'years', u'NNS'), (u'old', u'JJ'),
                (u'and', u'CC'), (u'former', u'JJ'), (u'chairman', u'NN'), (u'of', u'IN'),
                (u'Consolidated', u'NNP'), (u'Gold', u'NNP'), (u'Fields', u'NNP'),
                (u'PLC', u'NNP'), (u',', u','), (u'was', u'VBD'), (u'named', u'VBN'),
                (u'a', u'DT'), (u'nonexecutive', u'JJ'), (u'director', u'NN'), (u'of', u'IN'),
                (u'this', u'DT'), (u'British', u'JJ'), (u'industrial', u'JJ'),
                (u'conglomerate', u'NN'), (u'.', u'.')],
            [(u'A', u'DT'), (u'form', u'NN'),
                (u'of', u'IN'), (u'asbestos', u'NN'), (u'once', u'RB'), (u'used', u'VBN'),
                (u'to', u'TO'), (u'make', u'VB'), (u'Kent', u'NNP'), (u'cigarette', u'NN'),
                (u'filters', u'NNS'), (u'has', u'VBZ'), (u'caused', u'VBN'), (u'a', u'DT'),
                (u'high', u'JJ'), (u'percentage', u'NN'), (u'of', u'IN'),
                (u'cancer', u'NN'), (u'deaths', u'NNS'),
                (u'among', u'IN'), (u'a', u'DT'), (u'group', u'NN'), (u'of', u'IN'),
                (u'workers', u'NNS'), (u'exposed', u'VBN'), (u'to', u'TO'), (u'it', u'PRP'),
                (u'more', u'RBR'), (u'than', u'IN'), (u'30', u'CD'), (u'years', u'NNS'),
                (u'ago', u'IN'), (u',', u','), (u'researchers', u'NNS'),
                (u'reported', u'VBD'), (u'.', u'.')]]

print "Perceptron-"+str(accuracy(test,PerceptronTagger()))
print "NLTK-"+str(accuracy(test,NLTKTagger()))
print "Pattern-"+str(accuracy(test,PatternTagger()))
