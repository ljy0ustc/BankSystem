/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2022/5/10 16:15:53                           */
/*==============================================================*/


drop table if exists Account;

drop table if exists Branch;

drop table if exists ChequeAccount;

drop table if exists Client;

drop table if exists ClientOpenChequeAccount;

drop table if exists ClientOpenSavingAccount;

drop table if exists Contacts;

drop table if exists Department;

drop table if exists DepartmentManager;

drop table if exists Loan;

drop table if exists Pay;

drop table if exists Responsibility;

drop table if exists SavingAccount;

drop table if exists loan_to_client;

drop table if exists worker;

/*==============================================================*/
/* Table: Account                                               */
/*==============================================================*/
create table Account
(
   account_number       char(20) not null,
   branch_name          varchar(30) not null,
   account_balance      double not null,
   account_date         date not null,
   primary key (account_number)
);

/*==============================================================*/
/* Table: Branch                                                */
/*==============================================================*/
create table Branch
(
   branch_name          varchar(30) not null,
   city                 varchar(30) not null,
   primary key (branch_name)
);

/*==============================================================*/
/* Table: ChequeAccount                                         */
/*==============================================================*/
create table ChequeAccount
(
   account_number       char(20) not null,
   overdraft            double not null,
   primary key (account_number)
);

/*==============================================================*/
/* Table: Client                                                */
/*==============================================================*/
create table Client
(
   client_id            char(18) not null,
   client_name          varchar(10) not null,
   client_phone         varchar(15) not null,
   client_address       varchar(30) not null,
   primary key (client_id)
);

/*==============================================================*/
/* Table: ClientOpenChequeAccount                               */
/*==============================================================*/
create table ClientOpenChequeAccount
(
   account_number       char(20) not null,
   client_id            char(18) not null,
   last_visit_cheque_account date not null,
   primary key (account_number, client_id)
);

/*==============================================================*/
/* Table: ClientOpenSavingAccount                               */
/*==============================================================*/
create table ClientOpenSavingAccount
(
   client_id            char(18) not null,
   account_number       char(20) not null,
   last_visit_saving_account date not null,
   primary key (client_id, account_number)
);

/*==============================================================*/
/* Table: Contacts                                              */
/*==============================================================*/
create table Contacts
(
   client_id            char(18) not null,
   contact_name         varchar(20) not null,
   contact_phone        varchar(15) not null,
   contact_email        varchar(30) not null,
   contact_rel          varchar(20) not null,
   primary key (client_id)
);

/*==============================================================*/
/* Table: Department                                            */
/*==============================================================*/
create table Department
(
   department_id        char(2) not null,
   branch_name          varchar(30) not null,
   worker_id            char(18) not null,
   department_name      varchar(20) not null,
   department_type      varchar(10) not null,
   primary key (department_id)
);

/*==============================================================*/
/* Table: DepartmentManager                                     */
/*==============================================================*/
create table DepartmentManager
(
   worker_id            char(18) not null,
   department_id        char(2),
   primary key (worker_id)
);

/*==============================================================*/
/* Table: Loan                                                  */
/*==============================================================*/
create table Loan
(
   loan_id              char(20) not null,
   branch_name          varchar(30) not null,
   loan_money           double not null,
   pay_cnt              int not null,
   primary key (loan_id)
);

/*==============================================================*/
/* Table: Pay                                                   */
/*==============================================================*/
create table Pay
(
   pay_id               char(20) not null,
   loan_id              char(20) not null,
   pay_date             date not null,
   pay_money            double not null,
   primary key (pay_id)
);

/*==============================================================*/
/* Table: Responsibility                                        */
/*==============================================================*/
create table Responsibility
(
   client_id            char(18) not null,
   worker_id            char(18) not null,
   responsibility_type  bool not null,
   primary key (client_id, worker_id)
);

/*==============================================================*/
/* Table: SavingAccount                                         */
/*==============================================================*/
create table SavingAccount
(
   account_number       char(20) not null,
   interest_rate        double not null,
   currency_type        varchar(10) not null,
   primary key (account_number)
);

/*==============================================================*/
/* Table: loan_to_client                                        */
/*==============================================================*/
create table loan_to_client
(
   client_id            char(18) not null,
   loan_id              char(20) not null,
   primary key (client_id, loan_id)
);

/*==============================================================*/
/* Table: worker                                                */
/*==============================================================*/
create table worker
(
   worker_id            char(18) not null,
   department_id        char(2) not null,
   worker_name          varchar(10) not null,
   worker_phone         varchar(15) not null,
   worker_address       varchar(30) not null,
   work_date            date not null,
   primary key (worker_id)
);

alter table Account add constraint FK_establish_account foreign key (branch_name)
      references Branch (branch_name) on delete restrict on update restrict;

alter table ChequeAccount add constraint FK_CheckAccountInherence foreign key (account_number)
      references Account (account_number) on delete restrict on update restrict;

alter table ClientOpenChequeAccount add constraint FK_ClientOpenChequeAccount foreign key (account_number)
      references ChequeAccount (account_number) on delete restrict on update restrict;

alter table ClientOpenChequeAccount add constraint FK_ClientOpenChequeAccount2 foreign key (client_id)
      references Client (client_id) on delete restrict on update restrict;

alter table ClientOpenSavingAccount add constraint FK_ClientOpenSavingAccount foreign key (client_id)
      references Client (client_id) on delete restrict on update restrict;

alter table ClientOpenSavingAccount add constraint FK_ClientOpenSavingAccount2 foreign key (account_number)
      references SavingAccount (account_number) on delete restrict on update restrict;

alter table Contacts add constraint FK_ContactRel foreign key (client_id)
      references Client (client_id) on delete restrict on update restrict;

alter table Department add constraint FK_DepartmentAndBranch foreign key (branch_name)
      references Branch (branch_name) on delete restrict on update restrict;

alter table Department add constraint FK_DepartmentManager2 foreign key (worker_id)
      references DepartmentManager (worker_id) on delete restrict on update restrict;

alter table DepartmentManager add constraint FK_DepartmentManager foreign key (department_id)
      references Department (department_id) on delete restrict on update restrict;

alter table DepartmentManager add constraint FK_WorkerInherence foreign key (worker_id)
      references worker (worker_id) on delete restrict on update restrict;

alter table Loan add constraint FK_sent_loan foreign key (branch_name)
      references Branch (branch_name) on delete restrict on update restrict;

alter table Pay add constraint FK_pay_loan foreign key (loan_id)
      references Loan (loan_id) on delete restrict on update restrict;

alter table Responsibility add constraint FK_Responsibility foreign key (client_id)
      references Client (client_id) on delete restrict on update restrict;

alter table Responsibility add constraint FK_Responsibility2 foreign key (worker_id)
      references worker (worker_id) on delete restrict on update restrict;

alter table SavingAccount add constraint FK_SavingAccountInheritance foreign key (account_number)
      references Account (account_number) on delete restrict on update restrict;

alter table loan_to_client add constraint FK_loan_to_client foreign key (client_id)
      references Client (client_id) on delete restrict on update restrict;

alter table loan_to_client add constraint FK_loan_to_client2 foreign key (loan_id)
      references Loan (loan_id) on delete restrict on update restrict;

alter table worker add constraint FK_DepartmentAndWorkerRel foreign key (department_id)
      references Department (department_id) on delete restrict on update restrict;

