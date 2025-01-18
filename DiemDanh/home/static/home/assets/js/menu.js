document.addEventListener('DOMContentLoaded', function () {
    // Lấy đường dẫn hiện tại
    const currentPath = window.location.pathname;

    // Tìm tất cả các mục menu
    const menuItems = document.querySelectorAll('.menu-item');

    // Thêm class 'active' vào mục menu phù hợp
    menuItems.forEach(item => {
        const link = item.querySelector('a');
        if (link && link.getAttribute('href') && currentPath.includes(link.getAttribute('href'))) {
            item.classList.add('active');
        }
    });
});

