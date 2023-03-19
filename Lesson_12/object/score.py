from utils import *
class Score:
    def __init__(self, stu_id='', sub_id='', prog_score='', end_score='', final_score=''):
        self.stu_id = stu_id
        self.sub_id = sub_id
        self.prog_score = prog_score
        self.end_score = end_score
        self.final_score = final_score

    def display_menu(self):
        while True:
            print("--------------------------------")
            print("PLEASE SELECT A FUNCTION")
            print("1. ADD NEW SCORE")
            print("2. UPDATE SCORE")
            print("3. DELETE SCORE")
            print("4. SEARCH SCORE")
            print("5. SCORE STATISTICS")
            print("0. EXIT")
            key = input("ENTER YOUR CHOICE: ")
            if key == '1':
                self.add_score()
            elif key == '2':
                self.update_score()
            elif key == '3':
                self.delete_score()
            elif key == '4':
                self.search_score()
            elif key == '5':
                self.statistics_score()
            elif key == '0':
                print("EXITING ...")
                return
            else:
                print("INVALID CHOICE")
                print("PLEASE TRY AGAIN")

    def call_final_score(self):
        self.final_score = (int(self.prog_score) + int(self.end_score)*2)/3

    def input_score(self):
        self.prog_score = input("ENTER YOUR PROGRAM SCORE: ")
        self.end_score = input("END YOUR END SCORE: ")

    def add_score(self):
        print("--ADD SCORE--")
        self.stu_id = input("ENTER STUDENT ID: ")
        self.sub_id = input("ENTER SUBJECT ID: ")
        self.input_score()
        self.call_final_score()
        score_info = '|'.join([self.stu_id, self.sub_id, self.prog_score, self.end_score, str(self.final_score), '\n'])
        add_score_status = write_txt('data/scores.txt', [score_info], 'a+')
        if add_score_status:
            print("SCORE ADDED SUCCESSFULLY")
        else:
            print("SCORE ADDED FAILED")

    def update_score(self):
        while True:
            print("--UPDATE SCORE--")
            stu_id_input = input("ENTER STUDENT ID: ")
            sub_id_input = input("ENTER SUBJECT ID: ")
            score_infos = read_txt('data/scores.txt')
            for idx, sco in enumerate(score_infos):
                stu_id = sco.split('|')[0]
                sub_id = sco.split('|')[1]
                if stu_id_input == stu_id and sub_id_input == sub_id:
                    self.input_score()
                    self.call_final_score()
                    score_info = '|'.join([self.stu_id, self.sub_id, self.prog_score, self.end_score, str(self.final_score), '\n'])
                    score_infos[idx] = score_info
                    update_score_status = write_txt('data/scores.txt', score_infos, 'w+')
                    if update_score_status:
                        print("SCORE UPDATED SUCCESSFULLY")
                        return True
                    else:
                        print("SCORE UPDATED FAILED")
                        return False
                    
            print("STUDENT ID OR SUBJECT ID NOT FOUND")

    def delete_score(self):
        while True:
            print("--DELETE SCORE--")
            stu_id_input = input("ENTER STUDENT ID: ")
            sub_id_input = input("ENTER SUBJECT ID: ")
            
            score_infos = read_txt('data/scores.txt')

            for idx, sco in enumerate(score_infos):
                stu_id = sco.split('|')[0]
                sub_id = sco.split('|')[1]

                if sub_id_input == sub_id and stu_id_input == stu_id:
                    score_infos.pop(idx)
                    del_score_status = write_txt('data/scores.txt', score_infos, 'w+')
                    if del_score_status:
                        print("SCORE DELETED SUCCESSFULLY")
                        return True
                    else:
                        print("SCORE DELETED FAILED")
                        return False
            print("STUDENT ID OR SUBJECT ID NOT FOUND")

    def search_score(self):
        print("--SEARCH SCORE--")
        stu_id_input = input("ENTER STUDENT ID: ")
        sub_id_input = input("ENTER SUBJECT ID: ")

        score_infos = read_txt('data/scores.txt')
        for sco in score_infos:
            stu_id = sco.split('|')[0]
            sub_id = sco.split('|')[1]

            if stu_id_input == stu_id and sub_id_input == sub_id:
                print("SCORE INFORMATION")
                print(f"STUDENT ID: {stu_id}")
                print(f"SUBJECT ID: {sub_id}")
                print(f"PROGRAM SCORE: {sco.split('|')[2]}")
                print(f"END SCORE: {sco.split('|')[3]}")
                return
            print("STUDENT ID OR SUBJECT ID NOT FOUND")

    def statistics_score(self):
        score_a, score_b , score_c, score_d = [], [], [], []
        score_infos = read_txt('data/scores.txt')
        for sco in score_infos:
            finally_score = float(sco.split('|')[4])
            if finally_score >= 90 and finally_score <= 100:
                score_a.append(finally_score)
            elif finally_score >= 80 and finally_score < 90:
                score_b.append(finally_score)
            elif finally_score >= 50 and finally_score <70:
                score_c.append(finally_score)
            else:
                score_d.append(finally_score)

        score_a_str = "NUM OF A: " + str(len(score_a))
        score_b_str = "NUM OF B: " + str(len(score_b))
        score_c_str = "NUM OF C: " + str(len(score_c))
        score_d_str = "NUM OF D: " + str(len(score_d))
        score_statistics = ("\n").join([score_a_str, score_b_str, score_c_str, score_d_str])
        if write_txt('data/scores_statistic.txt', [score_statistics], 'w+'):
            print("WROTE SCORE STATISTICS INTO TXT FILE SUCCESSFULLY")
        else:
            print("WROTE SCORE STATISTICS INTO TXT FILE FAILED")