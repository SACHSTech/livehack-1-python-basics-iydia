print("\nWelcome to the popeyes chicken distributor.")
total_chicken = int(input("\nHow much chicken do you need to distribute?: "))
total_students = int(input("\nHow many students do you need to distribute it amongst?: "))
chicken_per_student = (total_chicken // total_students)
remainder = total_chicken - (chicken_per_student*total_students)
print("\nEach student receives " + str(chicken_per_student) + " chicken(s) and Mr. Fabroa will receive " + str(remainder) + " chicken(s).")