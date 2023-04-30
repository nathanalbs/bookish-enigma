import unittest
from final_project import Player, Queue, Stack, Tournament

class TestProgram(unittest.TestCase):
    def test_player_str(self):
        player = Player("nathan", "Bronze", 25)
        self.assertEqual(str(player), "nathan (Bronze, 25)")

    def test_enqueue_and_dequeue(self):
        q = Queue()
        p1 = Player("nathan", "Bronze", 25)
        p2 = Player("jacke", "Gold", 30)
        q.enqueue(p1)
        q.enqueue(p2)
        self.assertEqual(q.dequeue(), p1)
        self.assertEqual(q.dequeue(), p2)

    def test_remove_player(self):
        q = Queue()
        p1 = Player("nathan", "Bronze", 25)
        p2 = Player("jacke", "Gold", 30)
        q.enqueue(p1)
        q.enqueue(p2)
        self.assertEqual(q.remove_player("nathan"), p1)
        self.assertEqual(q.remove_player("jacke"), p2)
        self.assertTrue(q.is_empty())


    def test_push_and_pop(self):
        s = Stack()
        p1 = Player("nathan", "Bronze", 25)
        p2 = Player("jacke", "Gold", 30)
        s.push(p1)
        s.push(p2)
        self.assertEqual(s.pop(), p2)
        self.assertEqual(s.pop(), p1)

    def test_add_player(self):
        t1 = Tournament("League Championship Series")
        t1.add_player("nathan", "Bronze", 25)
        self.assertEqual(t1.players.items[0].name, "nathan")
        t2 = Tournament("All-Star Game")
        t2.add_player("jacke", "Gold", 30)
        self.assertTrue(t2.players.is_empty())

if __name__ == '__main__':
    unittest.main()
