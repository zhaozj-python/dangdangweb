/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/9/9 15:56:25                            */
/*==============================================================*/


drop table if exists t_address;

drop table if exists t_book;

drop table if exists t_cart;

drop table if exists t_category;

drop table if exists t_order;

drop table if exists t_order_item;

drop table if exists t_user;

/*==============================================================*/
/* Table: t_address                                             */
/*==============================================================*/
create table t_address
(
   id                   int not null auto_increment,
   name                 varchar(20),
   address              varchar(100),
   phone                varchar(20),
   postcode             varchar(6),
   telephone            varchar(20),
   user_id              int,
   primary key (id)
);

/*==============================================================*/
/* Table: t_book                                                */
/*==============================================================*/
create table t_book
(
   book_id              int not null auto_increment,
   book_name            varchar(20),
   book_cover           varchar(50),
   intro                varchar(200),
   comment              int,
   author               varchar(20),
   publish              varchar(20),
   date                 date,
   price                int,
   discount             int,
   sales                int,
   inventory            int,
   store                varchar(30),
   category_id          int,
   book_isbn            varchar(30),
   word_count           int,
   page_count           int,
   format               int,
   paper                varchar(20),
   recommend            varchar(300),
   author_intro         varchar(300),
   menu                 varchar(300),
   comments             varchar(500),
   primary key (book_id)
);

/*==============================================================*/
/* Table: t_cart                                                */
/*==============================================================*/
create table t_cart
(
   cart_id              int not null auto_increment,
   user_id              int,
   book_id              int,
   count                int,
   primary key (cart_id)
);

/*==============================================================*/
/* Table: t_category                                            */
/*==============================================================*/
create table t_category
(
   id                   int not null auto_increment,
   title                varchar(20),
   parentid             int,
   level                int,
   primary key (id)
);

/*==============================================================*/
/* Table: t_order                                               */
/*==============================================================*/
create table t_order
(
   order_id             int not null auto_increment,
   user_id              int,
   "order"              varchar(30),
   address_id           int,
   create_time          datetime,
   price                decimal,
   primary key (order_id)
);

/*==============================================================*/
/* Table: t_order_item                                          */
/*==============================================================*/
create table t_order_item
(
   id                   int not null auto_increment,
   order_id             int,
   book_id              int,
   count                int,
   primary key (id)
);

/*==============================================================*/
/* Table: t_user                                                */
/*==============================================================*/
create table t_user
(
   id                   int not null auto_increment,
   username             varchar(20),
   password             varchar(20),
   primary key (id)
);

alter table t_address add constraint FK_Reference_1 foreign key (user_id)
      references t_user (id) on delete restrict on update restrict;

alter table t_book add constraint FK_Reference_9 foreign key (category_id)
      references t_category (id) on delete restrict on update restrict;

alter table t_cart add constraint FK_Reference_12 foreign key (book_id)
      references t_book (book_id) on delete restrict on update restrict;

alter table t_cart add constraint FK_Reference_5 foreign key (user_id)
      references t_user (id) on delete restrict on update restrict;

alter table t_order add constraint FK_Reference_11 foreign key (address_id)
      references t_address (id) on delete restrict on update restrict;

alter table t_order add constraint FK_Reference_2 foreign key (user_id)
      references t_user (id) on delete restrict on update restrict;

alter table t_order_item add constraint FK_Reference_3 foreign key (order_id)
      references t_order (order_id) on delete restrict on update restrict;

alter table t_order_item add constraint FK_Reference_4 foreign key (book_id)
      references t_book (book_id) on delete restrict on update restrict;

