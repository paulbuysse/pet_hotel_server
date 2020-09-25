CREATE TABLE "owners" (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	CONSTRAINT "owners_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "pets" (
	"id" serial NOT NULL,
	"owner_id" int NOT NULL,
	"pet_name" varchar(255) NOT NULL,
	"breed" varchar(255) NOT NULL,
	"color" varchar(255) NOT NULL,
	"checked_in" BOOLEAN NOT NULL,
	"checked_date" DATE,
	CONSTRAINT "pets_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

ALTER TABLE "pets" ADD CONSTRAINT "pets_fk0" FOREIGN KEY ("owner_id") REFERENCES "owners"("id");

INSERT INTO owners (name)
VALUES ('Paul');
INSERT INTO owners (name)
VALUES ('Patrick');
INSERT INTO owners (name)
VALUES ('Jenni');
INSERT INTO owners (name)
VALUES ('Riley');

INSERT INTO pets (owner_id, pet_name, breed, color, checked_in, checked_date)
VALUES (1, 'Stanley', 'Tabby', 'Orange', false, '09-24-2020');
INSERT INTO pets (owner_id, pet_name, breed, color, checked_in, checked_date)
VALUES (2, 'Simon', 'Siamese', 'Grey', false, '09-02-2019');
INSERT INTO pets (owner_id, pet_name, breed, color, checked_in, checked_date)
VALUES (3, 'Buddy', 'Laborador', 'Black', false, '08-24-2020');
INSERT INTO pets (owner_id, pet_name, breed, color, checked_in, checked_date)
VALUES (4, 'Wanda', 'Unknown', 'White', false, '07-24-2020');