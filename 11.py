worker = {"홍길동", "이수지", "박상민", "강민우", "하누리"}
later = {"홍길동", "이수지", "박상민"}
absenter = {"박상민", "하누리"}
print("보너스를 받는 사원 : {0}".format(worker - later - absenter))
print("야근하는 사원 : {0}".format(later & absenter))
