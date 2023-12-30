import hashlib

username_trial = "MORTON"
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"


index = [4, 5, 3, 6, 2, 7, 1, 8]

for i in index:
    hashed_username = hashlib.sha256(username_trial.encode()).hexdigest()
    key_part_dynamic1_trial += hashed_username[i]

print(key_part_dynamic1_trial)
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key_full_template_trial)
