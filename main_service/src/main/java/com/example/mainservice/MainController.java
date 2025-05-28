package com.example.mainservice;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MainController {

    @GetMapping("/")
    public String index() {
        // This will implicitly serve src/main/resources/static/index.html
        // because of Spring Boot's default static content handling.
        return "index";
    }
}
