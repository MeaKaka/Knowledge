def train_model(
        learning_rate,
        steps,
        batch_size,
        training_example,
        training_targets,
        validation_examples,
        validation_targets
):
    periods=10
    steps_per_period = steps /periods
    # 线性回归
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients-by_norm(my_optimizer,5.0)
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns=construct_feature_columns(training_example),
        optimizer=my_optimizer
    )
    # 创建输入函数
    training_input_fn = lambda: my_optimizer_input_fn(
        training_example,
        training_targets["median_house_value"],
        batch_size=batch_size
    )
    predict_training_input_fn = lambda: my_input_fn(
        training_example,
        training_targets["median_house_value"],
        num_epochs=1,
        shuffle=False
    )
    predict_validation_input_fn = lambda: my_input_fn(
        validation_examples,
        validation_targets["median_house_value"],
        num_epochs=1,
        shuffle=False
    )

    print "Training model..."
    print "RMSE (on training data):"
    training_rmse = []
    validation_rmse = []
    for period in range(0,periods):
        linear_regressor.train(
            input_fn=training_input_fn,
            steps=steps_per_period
        )
    # 计算预测情况
    training_predictions = linear_regressor.predict(input_fn = predict_training_input_fn)
    training_predictions = np.array([item['predictions'][0] for item in training_predictions])
    validation_predictions = linear_regressor.predict(input_fn=predict_validation_input_fn)
    validation_predictions = np.array([item['predictions'][0] for item in validation_predictions])

