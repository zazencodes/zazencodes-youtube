sed -E 's/,(Workout_Type|Yoga|HIIT|Cardio|Strength)//g' gym_members_exercise_tracking.csv | head > gym_member_features_to_predict.csv
