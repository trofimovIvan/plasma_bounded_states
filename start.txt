FOR /L %%N IN (46, 1, 60) DO (
	equil.exe & track.exe & bound.exe
	python3 save.py --num=%%N
)
PAUSE