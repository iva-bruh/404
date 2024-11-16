<script>
  import Header from "../Header.svelte";
  import Footer from "../Footer.svelte";
	// Создаем массив с федеральными мерами поддержки и их краткими описаниями.
	const measures = [
		{
			title: 'Налоговые льготы',
			description:
				'ИТ-компании могут получать налоговые льготы на прибыль и имущество, что позволяет снизить налоговую нагрузку.',
			image: 'images/налоговые льготы.jpg'
		},
		{
			title: 'Льготные кредиты',
			description:
				'Малые и средние предприятия могут получить льготные кредиты на развитие IT-бизнеса с пониженной процентной ставкой.',
			image: 'images/льготные кредиты.jpg' // Замените на ваше изображение
		},
		{
			title: 'Гранты',
			description:
				'Компании могут участвовать в конкурсах и получать гранты на реализацию инновационных проектов.',
			image: 'images/гранты.jpg' // Замените на ваше изображение
		},
		{
			title: 'Субсидирование приобретения ПО для МСП',
			description:
				'Субъекты малого и среднего бизнеса могут приобрести российское ПО со скидкой 50%.',
			image: 'images/субсидирование.jpg' // Замените на ваше изображение
		},
		{
			title: 'Льготная ипотека',
			description: 'Специальные условия ипотечных кредитов для IT-специалистов и их семей.',
			image: 'https://example.com/images/mortgage.jpg' // Замените на ваше изображение
		},
		{
			title: 'Отсрочка от призыва',
			description:
				'IT-специалисты могут получать отсрочку от военной службы, что обеспечивает стабильность в работе.',
			image: 'https://example.com/images/military-delay.jpg' // Замените на ваше изображение
		},
		{
			title: 'Освобождение от проверок',
			description:
				'IT-компании могут быть освобождены от плановых проверок в течение определенного времени.',
			image: 'https://example.com/images/no-audit.jpg' // Замените на ваше изображение
		},
		{
			title: 'Трудоустройство и ВНЖ для иностранцев',
			description:
				'Упрощенные процедуры трудоустройства и получения вида на жительство для иностранных IT-специалистов.',
			image: 'https://example.com/images/employment.jpg' // Замените на ваше изображение
		},
		{
			title: 'Включение в реестры',
			description:
				'Компаниям предоставляется возможность включения в специальные реестры, что открывает доступ к дополнительным льготам.',
			image: 'https://example.com/images/register.jpg' // Замените на ваше изображение
		},
		{
			title: 'Аккредитация',
			description: 'Процедура аккредитации в целях получения государственных субсидий и льгот.',
			image: 'https://example.com/images/accreditation.jpg' // Замените на ваше изображение
		},
		{
			title: 'ИТ-образование',
			description: 'Поддержка образовательных программ и курсов для подготовки IT-специалистов.',
			image: 'https://example.com/images/education.jpg' // Замените на ваше изображение
		},
		{
			title: 'Привлечение финансирования',
			description:
				'Меры, направленные на помощь в привлечении частного и государственного финансирования для IT-компаний.',
			image: 'https://example.com/images/funding.jpg' // Замените на ваше изображение
		},
		{
			title: 'Поддержка особо значимых проектов',
			description:
				'Государственная поддержка для реализации крупных IT-проектов, имеющих стратегическое значение.',
			image: 'https://example.com/images/significant-projects.jpg' // Замените на ваше изображение
		}
	];
</script>
<Header/>
<div class="container">
	<h1>Федеральные меры поддержки в сфере IT</h1>
	{#each measures as measure}
		<div class="measure">
			<img src={measure.image} alt={measure.title} />
			<h2>{measure.title}</h2>
			<p>{measure.description}</p>
		</div>
	{/each}
</div>
<Footer/>
<style>
	.container {
		padding: 20px;
		max-width: 2000px;
		margin-left: auto;
		margin-right: auto;
	}
	h1 {
		text-align: center;
		margin-bottom: 30px;
		font-size: 25px;
	}

	.measure {
		border: 1px solid #ccc;
		border-radius: 8px;
		padding: 15px;
		margin: 15px 0;
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.measure img {
		width: 100%;
		max-width: 300px; /* Ограничиваем ширину изображения */
		border-radius: 8px;
		margin-bottom: 10px;
	}

	.measure h2 {
		margin: 10px 0;
		font-size: 1.5em;
		text-align: center;
	}

	.measure p {
		text-align: center;
		color: #555;
	}
</style>
