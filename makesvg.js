const fs = require('fs')



function main() {
	for (let i=0; i < 2010; i++) {
		var data = `
	        <svg viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
		    	<style>
	            	.Rrrrr { font: italic 24px serif; fill: red; }
	          	</style>
		        <text x="0" y="75" class="Rrrrr">${i}</text>
		    </svg>
		    `

		const path = `./${i}.svg`
		console.log(path)
		fs.writeFile(path, data, err => {
			if (err) {
				console.error(err)
				return
			}
		})
	}
}
main()
