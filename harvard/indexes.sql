CREATE INDEX "student_index" ON "students"("student_id","course_id");
CREATE INDEX "student_fall" ON "students"("id","name");
CREATE INDEX "student_course" ON "courses"("id","department","semester","tilte");
CREATE INDEX "cs_course" ON "courses" ("id");
CREATE INDEX "fall_2023" ON "students" ("id","name");
CREATE INDEX "requirement_index" ON "requirements" ("id","name");
CREATE INDEX "course_select" ON "courses" ("id","department","semester","title");
