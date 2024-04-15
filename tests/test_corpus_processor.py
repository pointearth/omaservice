import unittest
from app.corpus_processor import CorpusProcessor

class TestCorpusProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = CorpusProcessor()

    def test_create_single_corpus(self):
        documents = [
            "When Your Child Bites: How to Reduce or Stop This Behavior  Why Toddlers Bite Biting is a typical behavior often seen in infants, toddlers, and 2-year olds as a normal part of childhood development. Biting is both common and a normal part of childhood and a way for young children to test limits or express their feelings. Many children show signs of this behavior as early as their first birthday and usually stop biting when they are around 3 years of age. Very often, a child’s biting behavior is not due to",
            "biting behavior is not due to aggression, but rather due to an imbalance of the sensory system and poor self-regulation and impulse control.  Chewing and biting are both sensory activities tapping into the proprioceptive system which registers pressure in the joints of the jaw structure which has a regulating effect on a child’s nervous system. In simple terms, the child bites because they find it soothing.  Developmental factors which may cause a child to bite include:  Babies and toddlers bite for a"
        ]
        # expected_corpus = {
        #     'child', 'bite', 'reduce', 'stop', 'behavior', 'toddler', 'typical', 'seen', 'infant', '2-year', 'old', 'normal', 'part', 'childhood', 'development', 'common', 'way', 'young', 'test', 'limit', 'express', 'feeling', 'many', 'show', 'sign', 'early', 'first', 'birthday', 'usually', 'around', '3', 'year', 'age', 'often', 'due', 'aggression', 'rather', 'imbalance', 'sensory', 'system', 'poor', 'self-regulation', 'impulse', 'control', 'chewing', 'activity', 'tapping', 'proprioceptive', 'joint', 'jaw', 'structure', 'regulating', 'effect', 'nervous', 'simple', 'term', 'find', 'soothing', 'developmental', 'factor', 'may', 'cause', 'baby'
        # }
        expected_corpus = {
            'typical', 'include', 'way', 'stop', 'age', 'impulse', 'system', 'imbalance', 'biting', 'year', 'register', 'joint', 'development', 'part', 'express', 'feeling', 'soothing', 'rather', 'first', 'jaw', 'limit', 'childhood', 'usually', 'baby', 'infant', 'proprioceptive', 'child', 'developmental', 'regulating', 'common', 'factor', 'bite', '3', 'early', 'old', 'term', 'reduce', 'due', 'many', 'young', 'find', 'aggression', 'may', 'sign', 'show', 'pressure', 'simple', 'toddler', 'tapping', 'structure', 'often', 'poor', 'birthday', 'cause', 'effect', 'test', 'activity', 'nervous', 'control', 'normal', 'seen', 'around', 'behavior', 'chewing', 'sensory'
        }
        corpus = self.processor.create_single_corpus(documents)
        self.assertEqual(corpus, expected_corpus)

if __name__ == '__main__':
    unittest.main()