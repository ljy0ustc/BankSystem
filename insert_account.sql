INSERT INTO Branch(branch_name,city)
VALUES ('HEFEI','heifei');
INSERT INTO Branch(branch_name,city)
VALUES ('CHENGDU','chengdu');

INSERT INTO Account(account_number,branch_name,account_balance,account_date)
VALUES ('00000000000000000000','HEFEI','10000','2019-09-01');
INSERT INTO Account(account_number,branch_name,account_balance,account_date)
VALUES ('00000000000000000001','CHENGDU','20000','2019-09-02');

INSERT INTO SavingAccount(account_number,interest_rate,currency_type)
VALUES ('00000000000000000000','0.01','RMB');
INSERT INTO ChequeAccount(account_number,overdraft)
VALUES ('00000000000000000001','10000');

INSERT INTO ClientOpenChequeAccount(account_number,client_id,last_visit_cheque_account)
VALUES ('00000000000000000001','510105200101010005','2022-05-12');
INSERT INTO ClientOpenSavingAccount(account_number,client_id,last_visit_saving_account)
VALUES ('00000000000000000000','510105200101010006','2022-05-12');