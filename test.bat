@echo off
set list=1.1 1.5
for %%a in (%list%) do (
	for /L %%p in (1, 1, 5) do (
		python3 0909_plasma.py --phi=%%p --G=%%a
		MD Z2G%%a_phi%%p
		cd Z2G%%a_phi%%p
		FOR /L %%N IN (1, 1, 15) DO (
			equil.exe & track.exe & bound.exe
			python3 save.py --num=%%N
		)
		cd ..
	)
)
PAUSE