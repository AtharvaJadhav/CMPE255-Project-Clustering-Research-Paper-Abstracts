import sqlite3


class PaperDB():
    """
    Class to connect to sqlite3 database of research papers
    """
    def __init__(self, name="papers.db"):
        """
        name is the name of papers databes to connect to
        """

        self.name = name
        self.conn = sqlite3.connect(self.name)
        pass

    def getpapers(self, ids=[]):
        """
        ids is a list of integer research paper ids
        even a single id should be sent as an array of length 1
        returns an array with following structure
        [[int(id), str(title), str(abstract)], [...], [...]]
        """
        if len(ids) == 0:
            return None
        querystring = "select * from papers where id=?"
        answers = []
        for id in ids:
            ans = self.conn.execute(querystring, (id, ))
            ans = [r for r in ans]
            ans = list(ans[0])
            ans = ans[1:len(ans)]
            answers.append(ans)
        return answers

    def __del__(self):
        self.conn.close()


if __name__ == "__main__":
    name = "papers.db"
    p = PaperDB(name)
    print(p.getpapers([107210, 107212, 333071]))
        