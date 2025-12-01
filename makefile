help: 
	@echo "Commands:"
	@echo " - help: 	show this help"
	@echo " - new:		create a new file for today"
	@echo " - part2:	refresh instructions for current day (to get part 2)"
	@echo " - readme: 	build the new readme with links"

setup: 
	@touch session.cookie
	@mkdir -p inputs
	@make help

new: 
	@python src/utils/new_file.py

part2:
	@python src/utils/refresh_instructions.py

readme:
	@python src/utils/build_md.py