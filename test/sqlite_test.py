import unittest
import sqlite3

class SqliteTest(unittest.TestCase):
    def test_insert(self):
        conn = sqlite3.connect(r".\testdata\testdb.sqlite3")
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('SELECT * FROM customer ORDER BY id LIMIT 1;')
        row = c.fetchone()
        self.assertEqual(row['id'], 1)
        self.assertEqual(row['name'], "Paramod Sadalage")
        

if __name__ == '__main__':
    unittest.main()