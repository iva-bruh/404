<script>
	import Header from '../Header.svelte';
	import Footer from '../Footer.svelte';
	// Создаем массив с федеральными мерами поддержки и их краткими описаниями.
	const measures = [
		{
			title: 'Налоговые льготы: ставка в размере 0% при применении УСН',
			description:
				'В целях развития предпринимательской инициативы в IT-сфере установлена ставка (0%) по упрощенной системе налогообложения.',
			image: 'images/льгот0.jpg',
			conditiouns:'Налоговая ставка в размере 0% устанавливается для налогоплательщиков - индивидуальных предпринимателей, впервые зарегистрированных после вступления в силу настоящего Закона и применяющих упрощенную систему налогообложения, в отношении следующих видов предпринимательской деятельности: деятельность в области информационных технологий. Если за налоговый (отчетный) период средняя численность работников налогоплательщика - индивидуального предпринимателя, применяющего УСН, превысила 50 человек, то он утрачивает право на применение налоговой ставки в размере 0% по УСН.',
			documents:'услуга носит заявительный характер, применяется к правоотношениям, возникшим с 1 января 2022 года.',
			url:'Подробная информация тут: https://depit.admhmao.ru/mery-podderzhki-proektov/regionalnye-mery-podderzhki/7442155/predostavlenie-vychislitelnykh-moshchnostey-dlya-obucheniya-neyronnykh-setey-i-ili-testirovaniya-it-/'
		},
		{
			title:
				'Налоговые льготы: ставка в размере 1% при применении УСН с объектом налогообложения доходы',
			description:
				"В целях развития предпринимательской инициативы в IT-сфере на 2022-2024 годы установлена пониженная ставка (1%) по упрощенной системе налогообложения с объектом налогообложения 'доходы' для субъектов малого предпринимательства и индивидуальных предпринимателей.",
			image: 'images/льгот1.jpg',
			conditiouns:'Применяется в течение 2022-2024 годов для организаций и индивидуальных предпринимателей, являющихся правообладателями программ для электронных вычислительных машин, включенных в единый реестр российских программ для электронных вычислительных машин и баз данных, и (или) получивших документ о государственной аккредитации организации, осуществляющей деятельность в области информационных технологий.',
			documents:'Услуга носит заявительный характер, применяется к правоотношениям, возникшим с 1 января 2022 года.',
			url:'Подробная информация тут: https://depit.admhmao.ru/mery-podderzhki-proektov/regionalnye-mery-podderzhki/7442154/predostavlenie-vychislitelnykh-moshchnostey-dlya-obucheniya-neyronnykh-setey-i-ili-testirovaniya-it-/'
		},
		{
			title:
				'Налоговые льготы: ставка в размере 4% при применении УСН с объектом налогообложения доходы',
			description:
				"В целях развития предпринимательской инициативы в IT-сфере на 2023-2024 годы установлена пониженная ставка (4%) по упрощенной системе налогообложения с объектом налогообложения 'доходы' для субъектов малого предпринимательства и индивидуальных предпринимателей.",
			image: 'images/льгот2.jpg',
			conditiouns:'Применяется в течение 2023-2024 годов для субъектов малого предпринимательства и индивидуальных предпринимателей, основными видами экономической деятельности которых являются виды деятельности: разработка компьютерного программного обеспечения, консультационные услуги в данной области и другие сопутствующие услуги (класс 62) и деятельность в области информационных технологий (класс 63).',
			documents:'Услуга носит заявительный характер, применяется к правоотношениям, возникшим с 1 января 2023 года',
			url:'Подробная информация тут: https://depit.admhmao.ru/mery-podderzhki-proektov/regionalnye-mery-podderzhki/10489102/nalogovye-lgoty-stavka-v-razmere-4-pri-primenenii-/'
		},
		{
			title:
				'Налоговые льготы: ставка в размере 0% при применении патентной системы налогообложения',
			description:
				'В целях развития предпринимательской инициативы в IT-сфере установлена ставка (0%) ппри применении патентной системы налогообложения.',
			image: 'images/льгот3.png',
			conditiouns:'Налоговая ставка в размере 0% устанавливается для налогоплательщиков - индивидуальных предпринимателей, впервые зарегистрированных после вступления в силу настоящего Закона и применяющих патентную систему налогообложения, в отношении следующих видов предпринимательской деятельности: разработка компьютерного программного обеспечения, в том числе системного программного обеспечения, приложений программного обеспечения, баз данных, web-страниц, включая их адаптацию и модификацию.',
			documents:'Услуга носит заявительный характер, применяется к правоотношениям, возникшим с 1 января 2022 года',
			url:'Подробная информация тут: https://depit.admhmao.ru/mery-podderzhki-proektov/regionalnye-mery-podderzhki/10489107/nalogovye-lgoty-stavka-v-razmere-0-pri-primenenii-/'
		},
		{
			title:
				'Налоговые льготы: ставка в размере 5% при применении УСН с объектом налогообложения доходы, уменьшенные на величину расходов',
			description:
				'В целях развития предпринимательской инициативы на 2019-2024 годы установлена пониженная ставка (5%) по упрощенной системе налогообложения с объектом налогообложения «доходы, уменьшенные на величину расходов» для субъектов малого предпринимательства и индивидуальных предпринимателей.',
			image: 'images/льгот4.jpg',
			conditiouns:'Организации и индивидуальные предприниматели, применяющие упрощенную систему налогообложения.',
			documents:'услуга носит заявительный характер.',
			url:'Подробная информация тут: https://depit.admhmao.ru/mery-podderzhki-proektov/regionalnye-mery-podderzhki/7442149/predostavlenie-vychislitelnykh-moshchnostey-dlya-obucheniya-neyronnykh-setey-i-ili-testirovaniya-it-/'
		},
		{
			title:
				'Предоставление социальных выплат отдельным категориям граждан на обеспечение жилыми помещениями',
			description:
				'Социальные выплаты предоставляются работникам организаций, являющихся субъектами малого и среднего предпринимательства, или индивидуальным предпринимателям, зарегистрированным в автономном округе, осуществляющим деятельность в области информационных технологий, компьютерного программного обеспечения и (или) участвующим в реализации проекта «Цифровая платформа Югры».',
			image: 'images/соцвыплаты.jpg',
			conditiouns:'Критерии участников: а) является гражданином Российской Федерации; б) является нуждающимся в жилом помещении; в) ранее не являлся получателем мер социальной поддержки на улучшение жилищных условий; г) осуществляет не менее 5 лет со дня получения социальной выплаты трудовую деятельность в автономном округе; д) постоянно проживает в автономном округе.',
			documents:'Перечень документов в соответствии с пунктом 58 приложения 7 постановления Правительства ХМАО – Югры от 29.12.2020 г. № 643-п «О мерах по реализации Государственной программы Ханты-Мансийского автономного округа - Югры «Развитие жилищной сферы».',
			url:'Подробная информация тут: https://depit.admhmao.ru/mery-podderzhki-proektov/regionalnye-mery-podderzhki/7442145/predostavlenie-vychislitelnykh-moshchnostey-dlya-obucheniya-neyronnykh-setey-i-ili-testirovaniya-it-/'
		},
		{
			title: 'Инвестиционный налоговый вычет',
			description:
				'Введен инвестиционный налоговый вычет в размере 70% для телекоммуникационных компаний.  Таким образом им вернут часть налога на прибыль. Это поможет сохранить качество связи, не привлекая дополнительного финансирования, а также сохранит инвестиции операторов в эксплуатацию и модернизацию сетей связи.',
			image: 'images/вычет.png',
			conditiouns:'Инвестиционный налоговый вычет устанавливается в размере 70 процентов суммы расходов, указанных в абзаце втором пункта 1 и пункте 2 статьи 257 Налогового кодекса Российской Федерации (за исключением расходов на ликвидацию основных средств), для организаций или обособленных подразделений организаций, расположенных на территории автономного округа и осуществляющих деятельность в области информации и связи.',
			documents:'Инвестиционный налоговый вычет не применяется в отношении организаций, не представивших в уполномоченный Правительством Ханты-Мансийского автономного округа - Югры исполнительный орган государственной власти Ханты-Мансийского автономного округа - Югры информацию для оценки эффективности налоговых расходов Ханты-Мансийского автономного округа - Югры за налоговый (отчетный) период в срок, не превышающий десяти рабочих дней, следующих за днем окончания срока, установленного законодательством о налогах и сборах для представления налоговых деклараций в налоговые органы.',
			url:'Подробная информация тут: https://depit.admhmao.ru/mery-podderzhki-proektov/regionalnye-mery-podderzhki/10489109/investitsionnyy-nalogovyy-vychet/'
		},
		{
			title: 'Снижение ставки арендной платы',
			description:
				'В 2 раза снижена ставка арендной платы по договорам аренды имущества, находящегося в государственной собственности автономного округа для объектов связи и центров обработки данных.',
			image: 'images/арендная.jpg',
			conditiouns:'Ставка снижена для объектов связи и центров обработки данных.',
			documents:'Порядок не распространяется на отношения, возникшие при предоставлении в аренду: имущества, находящегося в хозяйственном ведении государственных предприятий автономного округа; имущества, находящегося в оперативном управлении государственных учреждений автономного округа; земельных участков, за исключением случаев одновременного предоставления (по одному договору) в аренду земельного участка и расположенных на нем зданий, строений и их частей, находящихся в собственности автономного округа; жилых помещений.',
			url:'Подробная информация тут: https://depit.admhmao.ru/mery-podderzhki-proektov/regionalnye-mery-podderzhki/7878501/snizhenie-stavki-arendnoy-platy/'

		},
		{
			title: 'Сумма налога на имущество уменьшается на 50%',
			description:
				'Сумма налога на имущество уменьшается на 50% для организаций, осуществляющих деятельность в области информационных технологий, начиная с отчетного периода получения документа о государственной аккредитации организации, осуществляющей деятельность в области информационных технологий, в отношении объектов связи и центров обработки данных.',
			image: 'images/имущество.jpg',
			conditiouns:'Льгота применяется для аккредитованных организаций, осуществляющих деятельность в области информационных технологий, в отношении объектов связи и центров обработки данных.',
			documents:'услуга носит заявительный характер',
			url:'Подробная информация тут: https://depit.admhmao.ru/mery-podderzhki-proektov/regionalnye-mery-podderzhki/10506197/summa-naloga-na-imushchestvo-umenshaetsya-na-50/'
		},
		{
			title: 'Конкурс на получение Грантов Губернатора ХМАО – Югры',
			description:
				'Ежегодно проводится конкурс на получение грантов Губернатора Ханты-Мансийского автономного округа – Югры на развитие гражданского общества и реализацию проектов в области культуры, искусства и креативных индустрий в направлении проектов в сфере ИКТ.',
			image: 'images/грант.jpg',
			conditiouns:'Участниками конкурса на получение грантов Губернатора ХМАО - Югры могут стать физические лица и ИП (граждане РФ, достигшие 18 лет), юридические лица (за исключением государственных учреждений, государственных корпораций, государственных компаний и политических партий). Участники конкурса должны быть зарегистрированы и осуществлять свою деятельность на территории ХМАО - Югры.',
			documents:'официальный сайт конкурса: https://грантгубернатора.рф. Перечень документов для участия размещается в конкурсной документации.',
			url:'Подробная информация тут: https://depit.admhmao.ru/mery-podderzhki-proektov/regionalnye-mery-podderzhki/10489110/konkurs-na-poluchenie-grantov-gubernatora-khmao-yu/'
		}
	];
	let selectedMeasure = null; // State to track the selected measure
	let isOverlayVisible = false; // State to control overlay visibility

	function openOverlay(measure) {
		selectedMeasure = measure;
		isOverlayVisible = true; // Show the overlay
	}

	function closeOverlay() {
		isOverlayVisible = false; // Hide the overlay
		selectedMeasure = null; // Clear the selected measure
	}
</script>

<Header />

<h1>Региональные меры поддержки в сфере IT</h1>

<div class="container">
	{#each measures as measure}
		<div
			class="measure"
			role="button"
			tabindex="0"
			on:click={() => openOverlay(measure)}
			on:keypress={(event) => event.key === 'Enter' && openOverlay(measure)}
		>
			<img src={measure.image} alt={measure.title} />
			<h2>{measure.title}</h2>
			<p>{measure.description}</p>
		</div>
	{/each}
</div>

{#if isOverlayVisible}
    <div class="overlay" role="dialog" aria-modal="true" on:click={closeOverlay}>
        <div class="overlay-content" on:click={e => e.stopPropagation()}>
			<h2>Условия получения поддержки, получатели</h2>
            <p class="mb-2">{selectedMeasure.conditiouns}</p>
			<h2>Перечень необходимых документов:</h2><p>{selectedMeasure.documents}</p>
			<p>{selectedMeasure.url}</p>
            <button class="close-button" on:click={closeOverlay}>Закрыть</button> <!-- Add the class here -->
        </div>
    </div>
{/if}

<Footer />

<style>
	.container {
		max-width: 1200px; /* Максимальная ширина контейнера */
		margin: 0 auto; /* Центрирование контейнера */
		padding: 30px 20px; /* Отступ для контейнера */
		display: grid; /* Используем сетку */
		grid-template-columns: repeat(4, 1fr); /* 4 равные колонки */
		gap: 20px; /* Промежутки между элементами */
		border-radius: 10px; /* Закругления контейнера */
		background-color: #d7ffd28f; /* Фон контейнера */
		box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Тень для контейнера */
	}

	h1 {
		text-align: center;
		margin-bottom: 30px;
		font-size: 2em; /* Увеличенный размер */
		font-weight: bold; /* Полужирное начертание заголовка */
		color: #ebe7e7; /* Цвет заголовка */
		padding: 10px;
		background: linear-gradient(
			270deg,
			#0c6d0f,
			#0f9e20,
			#0c6d0f
		); /* Градиент фона (синий и голубой) */
		background-size: 400% 400%; /* Увеличиваем размер градиента для анимации */
		animation: gradientAnimation 5s ease infinite; /* Анимация градиента */
		border-radius: 0 0 10px 10px; /*Закругление углов заголовка */
		box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2); /* Тень для заголовка */
	}
	h2{
		font-size: 18px;
		font-weight: 600;
		margin-bottom: 5px;
	}
	@keyframes gradientAnimation {
		0% {
			background-position: 0% 50%; /* Начальная позиция фона */
		}
		50% {
			background-position: 100% 50%; /* Позиция фона в середине анимации */
		}
		100% {
			background-position: 0% 50%; /* Конечная позиция фона */
		}
	}
	.measure {
		border-radius: 10px; /* Закругленные углы карточек */
		overflow: hidden; /* Скрывать переполнение */
		background-color: #ffffff; /* Белый фон для карточек */
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Тень для карточек */
		transition: transform 0.3s; /* Плавный эффект при изменении масштаба */
		position: relative; /* Для абсолютного позиционирования заголовка */
		padding: 15px; /* Внутренние отступы карточки */
		text-align: center; /* Выравнивание текста по центру */
		border: 1px solid #e0e0e0; /* Легкая граница вокруг карточек */
	}

	.measure:hover {
		transform: scale(1.05); /* Увеличение карточки при наведении */
	}

	img {
		width: 100%; /* Растягиваем на всю ширину контейнера */
		height: 200px; /* Автоматическая высота с сохранением пропорций */
		max-height: 180px; /* Максимальная высота изображения */
		object-fit: cover; /* Обрезка изображения для заполнения блока */
		border-bottom: 4px solid #0c6d0f; /* Цветовая граница снизу изображения */
		transition: filter 0.3s; /* Плавный переход между эффектами */
	}

	.measure:hover img {
		filter: brightness(70%); /* Затемнение изображения при наведении */
	}

	.measure h2 {
		margin-top: 10px; /* Отступ сверху заголовка */
		margin-bottom: 10px; /* Отступ снизу заголовка */
		font-size: 1.2em; /* Размер шрифта заголовка */
		color: #0c6d0f; /* Цвет текста заголовка */
		font-weight: bold; /* Полужирный текст */
		text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.2); /* Тень для текста заголовка */
	}

	.measure p {
		font-size: 0.95em; /* Размер шрифта для описания */
		color: #555; /* Цвет текста описания */
		line-height: 1.5; /* Высота строки для лучшей читаемости */
		margin: 0; /* Убираем отступы */
	}
	.overlay {
		position: fixed; /* Fixed positioning to cover the entire viewport */
		top: 0; /* Position at the top */
		left: 0; /* Position at the left */
		width: 100%; /* Cover the full width */
		height: 100%; /* Cover the full height */
		background: rgba(0, 0, 0, 0.7); /* Semi-transparent background for dimming effect */
		display: flex; /* Use flexbox to center overlay content */
		justify-content: center; /* Center the content horizontally */
		align-items: center; /* Center the content vertically */
		z-index: 1000; /* Ensure it's on top of everything */
	}

	.overlay-content {
		background: white; /* Background for the content area */
		padding: 20px; /* Inner spacing */
		border-radius: 8px; /* Rounded corners for the overlay */
		width: 450px; /* Set a specific width for the content */
		height: 450px; /* Set a specific height for the content */
		display: flex; /* Use flexbox for layout */
		flex-direction: column; /* Stack children vertically */
		justify-content: space-between; /* Space between items */
		overflow-y: auto; /* Scroll if content exceeds height */
	}

	.close-button {
		margin-top: auto; /* Pushes the button to the bottom */
		align-self: center; /* Center the button horizontally */
		padding: 10px 20px; /* Padding for the button */
		background-color: #0c6d0f; /* Button background color */
		color: white; /* Button text color */
		border: none; /* Remove border */
		border-radius: 5px; /* Rounded corners for the button */
		cursor: pointer; /* Pointer cursor on hover */
		margin-top: 10px;
	}

	.close-button:hover {
		background-color: #0f9e20; /* Lighter background on hover */
	}
	
</style>
