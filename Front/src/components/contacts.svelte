<script>
    import Header from "./Header.svelte";
    import Footer from "./Footer.svelte";

    const contacts = [
        {
            name: "Иван Иванов",
            position: "Директор",
            email: "ivan.ivanov@example.com",
            phone: "+7 (123) 456-78-90"
        },
        {
            name: "Мария Петрова",
            position: "Маркетолог",
            email: "maria.petrova@example.com",
            phone: "+7 (123) 456-78-91"
        },
        {
            name: "Сергей Сидоров",
            position: "Разработчик",
            email: "sergey.sidorov@example.com",
            phone: "+7 (123) 456-78-92"
        },
        {
            name: "Анна Смирнова",
            position: "Дизайнер",
            email: "anna.smirnova@example.com",
            phone: "+7 (123) 456-78-93"
        }
    ];
</script>

<Header />

<style>
    .contacts-page {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 600px; /* Максимальная ширина страницы контактов */
        margin: 20px auto; /* Центрируем страницу по горизонтали */
    }

    h2 {
        text-align: center;
        margin-bottom: 20px;
    }

    .contact {
        border-bottom: 1px solid #ccc;
        padding: 10px 0;
    }

    .contact:last-child {
        border-bottom: none; /* Убираем нижнюю границу у последнего контакта */
    }

    .contact h3 {
        margin: 0;
        font-size: 18px;
    }

    .contact p {
        margin: 5px 0;
        font-size: 14px;
    }
</style>

<div class="contacts-page">
    <h2>Контакты</h2>
    {#each contacts as contact}
        <div class="contact">
            <h3>{contact.name}</h3>
            <p><strong>Должность:</strong> {contact.position}</p>
            <p><strong>Email:</strong> {contact.email}</p>
            <p><strong>Телефон:</strong> {contact.phone}</p>
        </div>
    {/each}
</div>

<Footer />