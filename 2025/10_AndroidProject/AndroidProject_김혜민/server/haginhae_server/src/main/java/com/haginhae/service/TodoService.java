package com.haginhae.service;

import com.haginhae.entity.Todo;
import com.haginhae.repository.TodoRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class TodoService {

    private final TodoRepository todoRepository;

    public List<Todo> findAll() {
        return todoRepository.findAll();
    }

    public Todo create(Todo todo) {
        return todoRepository.save(todo);
    }

    public Todo update(Long id, Todo updatedTodo) {
        return todoRepository.findById(id)
            .map(todo -> {
                todo.setTitle(updatedTodo.getTitle());
                todo.setCompleted(updatedTodo.isCompleted());
                return todoRepository.save(todo);
            })
            .orElseThrow(() -> new IllegalArgumentException("할 일을 찾을 수 없습니다: id = " + id));
    }
    
    public void deleteTodo(Long id) {
        todoRepository.deleteById(id);
    }
}
