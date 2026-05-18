public class BadLoginTest {

    public void shouldLoginWithValidUser() throws InterruptedException {
        driver.findElement(By.id("username")).sendKeys("admin");
        driver.findElement(By.id("password")).sendKeys("123456");

        Thread.sleep(5000);

        driver.findElement(By.id("login-button")).click();
    }
}