import re, os

dir_path = os.path.dirname(os.path.realpath(__file__))

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if(f == 'logConvertor.py') : continue
    if(f == 'logConvertor.pyproj') : continue

    file_path = dir_path + '\\' + f
    real_file = open(file_path, 'r')
    while True:
        line = real_file.readline()
        if not line: break
        
        replaced = re.sub('^(.*Character::.*)|(.*LoadFieldNaviMeshResource.*)|(.*FriendLifeDispatcher::.*)|(.*FieldResource::.*)|(.*BattleDispatcher::.*)|(.*Field::.*)|(.*Fsm::.*)|(.*SkillWatcher::.*)|(.*BattleService::.*)^(\s*)',
                  '',
                  line)

        if not replaced.strip(): continue
        print(replaced)

    real_file.close()
