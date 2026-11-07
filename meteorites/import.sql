-- Create temporary table
CREATE TABLE "meteorites_temp"(
  "name" TEXT,
  "id" INTEGER,
  "nametype" TEXT,
  "class" TEXT,
  "mass" REAL,
  "discovery" TEXT,
  "year" INTEGER,
  "lat" REAL,
  "long" REAL,
  PRIMARY KEY("id")
);

-- Import CSV (run in SQLite CLI, not inside SQL file)
.import --csv --skip 1 meteorites.csv meteorites_temp


-- Clean up missing values
UPDATE "meteorites_temp" SET "mass" = NULL WHERE "mass" = '';
UPDATE "meteorites_temp" SET "year" = NULL WHERE "year" = '';
UPDATE "meteorites_temp" SET "lat" = NULL WHERE "lat" = '';
UPDATE "meteorites_temp" SET "long" = NULL WHERE "long" = '';

-- Round numeric columns
UPDATE "meteorites_temp" SET "mass" = ROUND("mass", 1);
UPDATE "meteorites_temp" SET "lat" = ROUND("lat", 1);
UPDATE "meteorites_temp" SET "long" = ROUND("long", 1);

-- Remove unwanted records
DELETE FROM "meteorites_temp" WHERE "nametype" = 'Relict';

-- Remove the 'nametype' column
ALTER TABLE "meteorites_temp" DROP COLUMN "nametype";

-- Drop old final table if exists
DROP TABLE IF EXISTS "meteorites";

-- Create cleaned final table
CREATE TABLE "meteorites" (
  "id" INTEGER PRIMARY KEY,
  "name" TEXT,
  "class" TEXT,
  "mass" REAL,
  "discovery" TEXT,
  "year" INTEGER,
  "lat" REAL,
  "long" REAL
);

-- Insert cleaned data
INSERT INTO "meteorites" ("name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "name", "class", "mass", "discovery", "year", "lat", "long"
FROM "meteorites_temp"
ORDER BY "year", "name";

-- Drop temporary table
DROP TABLE "meteorites_temp";
